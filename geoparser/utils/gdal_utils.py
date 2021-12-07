from osgeo import gdal
from osgeo import gdalconst
import numpy as np

def translate_geotiff(source_file_name, destination_file_name, create_jpeg = True):
    ds = gdal.Open(source_file_name)
    jpeg_file_name = destination_file_name.replace(".TIF", ".png").replace(".tif", ".png")
    #  gdal_translate -ot Byte -of png -srcwin 2200 1500 1000 1000 -scale 1 65455 0 255
    #  ./landsat_data/LC08_L2SP_030031_20210927_20211001_02_T1_SR_B1.TIF
    #  ./results/LC08_L2SP_030031_20210927_20211001_02_T1_SR_B1.png

    offsets = [2000, 2500, 1000, 800]
    print(">>> Writing ", destination_file_name)
    tiff = gdal.Translate(destination_file_name, ds, srcWin=offsets)
    tiff.FlushCache()

    jpg = gdal.Translate(jpeg_file_name, ds, outputType=gdalconst.GDT_Byte, format="png", srcWin=offsets,
                         scaleParams=[[]])
    print(">>> Writing ", jpeg_file_name)
    jpg.FlushCache()

def save_tiff_file(file_name, data, create_jpeg = True):
    driver = gdal.GetDriverByName("GTiff")

    rows = len(data[0])
    cols = len(data)

    outdata = driver.Create(file_name, rows, cols, 1, gdal.GDT_UInt16)

    outdata.GetRasterBand(1).WriteArray(data)
    print(outdata.GetRasterBand(1).GetStatistics(True, True))

    jpeg_file_name = file_name.replace(".TIF", ".png").replace(".tif", ".png")

    ds = gdal.Translate(jpeg_file_name, outdata, bandList=[1], rgbExpand="gray", scaleParams=[[]])
    print("NEWDATA:::", ds.GetRasterBand(1).GetStatistics(True, True))

    ds.FlushCache()
    outdata.FlushCache()  ##saves to disk!!



    outdata = None

def load_tiff_data(file_name):
    dataset = gdal.Open(file_name)
    data = dataset.ReadAsArray().astype(np.float)
    n_data = data[2200:3200, 1500:2500]
    del dataset
    return n_data