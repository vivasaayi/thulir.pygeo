import numpy as np

class IndexCalculator:
    def calculate_ndwi(self, band5, band6):
        print("Calculating NDVI")

        height = len(band5)
        width = len(band5[0])


        ndwi_o = np.zeros((height, width))

        for row in range(0, width):
            for col in range(0, height):
                b5_val = band5[row][col]
                b6_val = band6[row][col]
                ndwi = (b5_val - b6_val)/(b5_val + b6_val)
                ndwi_o[row][col] = ndwi * 1000

        return ndwi_o

    def calculate_mndwi(self, band3, band6):
        print("Calculating NDVI")

        height = len(band3)
        width = len(band3[0])

        mndwi_o = np.zeros((height, width))

        for row in range(0, width):
            for col in range(0, height):
                b3_val = band3[row][col]
                b6_val = band6[row][col]
                mndwi = (b3_val - b6_val)/(b3_val + b6_val)
                mndwi_o[row][col] = mndwi * 1000

        return mndwi_o

    def calculate_indices(self, band_data):
        print("Calculating Indices")
        ndwi = self.calculate_ndwi(band_data["b5"], band_data["b6"])
        mndwi = self.calculate_ndwi(band_data["b3"], band_data["b6"])

        indices = {
            "ndwi": ndwi,
            "mndwi": mndwi
        }

        return indices
