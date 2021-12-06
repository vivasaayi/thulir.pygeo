from glob import glob
import os
import json
import numpy as np
from osgeo import gdal
import scipy.misc as sm

import matplotlib.pyplot as plt

def pad_year_day(year, day):
    day_str = str(day) + ""
    
    if(len(day_str) == 1):
        day_str = day_str.rjust(3, "0")   
    elif(len(day_str) == 2):
        day_str = day_str.rjust(3, "0")   

    return year + day_str

def get_bands_for_date(year, day):
    day_str = pad_year_day(year, day)
    dirs = os.listdir("./data/" + day_str)

    result = {}

    for f in dirs:
        if(f.endswith("qa.TIF")):
            continue
        elif(not f.endswith(".TIF")):
            continue
        band = f.split("_")[1].replace(".TIF", "")

        result[band] = os.path.join("./data", day_str,f)

    return result

def extract_time_profile():
    day_range = range(1,10)
    year = "2020"

    band_data = {
    }

    # profiles[100, 100, 10] = 121
    # print(profiles)
    # print(profiles[100, 100, 10])

    bands = ["B01", "B02", "B03", "B04", "B05", "B06", "B06", "B07"]

    for b in bands:
        print("Band:", b)
        b_data = []
        for day in day_range:    
            file_names = get_bands_for_date(year, day)
            if(b not in file_names):
                print("Band Name Not found")
                continue
            
            b_file_name = file_names[b]
            print(b_file_name)

            dataset = gdal.Open(b_file_name) 
            data = dataset.ReadAsArray().astype(np.float)
            b_data.append(data)

        b_data_3d = np.dstack(b_data)

        band_data[b] = b_data_3d

    print(band_data)
    return
            
extract_time_profile()
  

# landsat_post_fire_path = "/tmp"

# path = os.path.join(landsat_post_fire_path, "*")
# glob(path)

# def norm(band):
#     band_min, band_max = band.min(), band.max()
#     return ((band - band_min)/(band_max - band_min))

# b2_file = glob(path + '**B3.TIF') # blue band
# b3_file = glob(path + '**B7.TIF') # green band
# b4_file = glob(path + '**10.TIF') # red band

# print(b2_file)
# print(b3_file)
# print(b4_file)

dataset = gdal.Open("MCD43A4.A2020151.h10v04.006.2020161013749_B03.TIF")
# print(json.dumps(dataset.GetDriver(), indent=2))
print(dataset.GetDriver().LongName)
print(dataset.GetDriver().ShortName)
print("Raster Count:", dataset.RasterCount)
print("Raster X:", dataset.RasterXSize)
print("Raster Y:", dataset.RasterYSize)
print("Projection is {}".format(dataset.GetProjection()))
print(json.dumps(dataset.GetDriver().GetDescription(), indent=2))

file_data = dataset.ReadAsArray().astype(np.float)

print(len(file_data))
print(len(file_data[0]))

# for item in file_data[0]:
#     print(item)

ds

plt.imshow(file_data)
plt.savefig('1.png')

print("Saved1")

file_link = gdal.Open("MCD43A4.A2020151.h10v04.006.2020161013749_B03.TIF")
file_data = file_link.ReadAsArray().astype(np.float)
plt.imshow(file_data, cmap='gray')
plt.savefig('2.png')
print("Saved2")