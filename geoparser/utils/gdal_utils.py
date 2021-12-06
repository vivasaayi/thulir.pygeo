from osgeo import gdal
import numpy as np

def save_tiff_file(file_name, data):
    driver = gdal.GetDriverByName("GTiff")

    rows = len(data[0])
    cols = len(data)

    outdata = driver.Create(file_name, rows, cols, 1, gdal.GDT_UInt16)

    outdata.GetRasterBand(1).WriteArray(data)

    outdata.FlushCache()  ##saves to disk!!
    outdata = None

def load_tiff_data(file_name):
    dataset = gdal.Open(file_name)
    data = dataset.ReadAsArray().astype(np.float)
    n_data = data[2200:3200, 1500:2500]
    del dataset
    return n_data