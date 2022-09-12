# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:02:38 2022

@author: nahmad
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

data = Dataset(r'C:/Users/nahmad/Downloads/GK2_GEMS_L2_20220801_2345_O3P_HK_DPRO_BIN4x4.nc')

# Accessing the variables

data1 = data.groups['Data Fields']
data2 = data.groups['Geolocation Fields']
time_data = data2.variables['Time'][:]
lon_data = data2.variables['Longitude'][:]
lat_data = data2.variables['Latitude'][:]
no2_data = data1.variables['ColumnAmountO3'][:]


mp = Basemap(projection = 'merc',
             llcrnrlon = 114.050397,
             llcrnrlat = 22.225503,
             urcrnrlon = 114.242058,
             urcrnrlat = 22.359781,
             resolution = 'i')

lon, lat = np.meshgrid(lon_data, lat_data)
x,y = mp(lon, lat)

c_scheme = mp.pcolor(x, y, cmap = 'jet')
mp.drawcoastlines()
mp.drawcounties()
mp.drawstates()

plt.title('no2')
plt.show()