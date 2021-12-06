import os.path

import os
import numpy as np
from osgeo import gdal

from geoparser.services.aws.s3 import S3Client
from geoparser.utils import file_utils
from geoparser.utils import gdal_utils
from geoparser.services.processing.index_calculator import  IndexCalculator

class LandsatDataUtils:
    def __init__(self):
        self._bucket = "landsat-dataasets"
        self.landsat_data_base_path = "./landsat_data"
        print("Initializing Landsat Data Utils")

    def extract_tiles(self, dirname, targetdir):
        source_files = file_utils.get_files_in_folder(dirname);
        destination_files = file_utils.get_files_in_folder(targetdir);

        for source_file in source_files:
            if source_file in destination_files:
                print("File {} already processed".format(source_file))
                continue
            self.extract_tile(source_files[source_file], targetdir)


    def extract_tile(self, source_file, destination_folder):
        source_file_name = source_file["fileName"]
        source_file_path = source_file["filePath"]

        if not file_utils.file_exists(source_file_path):
            print("File not exists ->  ", file_utils)
            return

        if ".TIF" not in source_file_name:
            print("Not a TIFF file --> ", source_file)
            return

        print("Processing file", source_file)
        dataset = gdal.Open(source_file_path)
        data = dataset.ReadAsArray().astype(np.float)
        n_data = data[2200:3200, 1500:2500]
        del dataset
        gdal_utils.save_tiff_file(os.path.join(destination_folder, source_file_name), n_data)

    def download_file(self, file_name, destination_folder):
        os.makedirs(destination_folder, exist_ok=True)
        target_file_name = os.path.join(destination_folder, file_name)

        if file_utils.file_exists(target_file_name):
            print("Target file name already exists ->  ", file_utils)
            return

        print('Downloading file {} to {}'.format(file_name, target_file_name))
        s3_client = S3Client()
        s3_client.download_file(self._bucket, file_name, target_file_name)

    def get_band_file_names(self, file_pattern):
        # This can be extracted from the mtl.json
        band_file_names = {}

        for ix in range(1, 11):
            if(ix == 9 or ix == 8):
                continue
            key = "b" + str(ix)
            band_file_names[key] = os.path.join(self.landsat_data_base_path, file_pattern + "_T1_SR_B" + str(ix) + ".TIF")

        return band_file_names

    def load_band_data(self, band_files):
        band_data = {}
        for b in band_files:
            try:
                data = gdal_utils.load_tiff_data(band_files[b])
                band_data[b] = data
            except Exception as ex:
                print(ex)

        return band_data

    def calculate_ndvi(self, file_pattern):
        print("Calculating NDVI")
        band_files = self.get_band_file_names((file_pattern))
        band_data = self.load_band_data(band_files)

        ix_calculator = IndexCalculator()
        indices = ix_calculator.calculate_indices(band_data)

        destination_pattern = os.path.join(self.landsat_data_base_path, file_pattern)

        gdal_utils.save_tiff_file(destination_pattern + "_ndwi.tiff", indices["ndwi"])
        gdal_utils.save_tiff_file(destination_pattern + "_mndwi.tiff", indices["mndwi"])



