import os
from glob import glob
import matplotlib.pyplot as plt
import rasterio as rio
from rasterio.plot import show


class Visualizer:
    """ Visualizes the generated raster file. """
    def __init__(self):
        # sets the location of the raster file
        self.raster_file = "../so_platte.tif"

    def visualize_raster(self):
        # plots the raster file in rgb and in grey scale
        raster_src = rio.open(self.raster_file)
        fig, (axrgb, axraster) = plt.subplots(1, 2, figsize=(14,7))
        show((raster_src), cmap='Greys_r', contour=True, ax=axrgb)
        show((raster_src),ax=axraster)
        plt.show()