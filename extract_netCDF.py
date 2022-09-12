from netCDF4 import Dataset
import numpy as np
import pandas as pd

# Reading in the netCDF file 
data = Dataset(r'C:/Users/nahmad/Downloads/GK2_GEMS_L2_20220801_0045_O3P_FC_DPRO_BIN4x4.nc', 'r')
#print(data.groups)

# Displaying the names of the variables
#print(data.groups.keys())

# Accessing the variables

data1 = data.groups['Data Fields']
#print(data1)

data2 = data.groups['Geolocation Fields']
#print(data2)

lon = data2.variables['Longitude']
#print(lon)

lat = data2.variables['Latitude']
#print(lat)

time = data2.variables['Time']
#print(time)

NO2 = data1.variables['ColumnAmountO3']
#print(NO2)


# Accessing the data from variables

time_data = data2.variables['Time'][:]
#print(time_data)

lon_data = data2.variables['Longitude'][:]
#print(lon_data)

lat_data = data2.variables['Latitude'][:]
#print(lat_data)

no2_data = data1.variables['ColumnAmountO3'][:]
#print(no2_data)

# storing the lat and lon into variables
lat_s = float(46)
lon_s = float(143)

#sq_difference
sq_diff_lat = (lat_data - lat_s)**2
sq_diff_lon = (lon_data - lon_s)**2

min_index_lat = sq_diff_lat.argmin()
min_index_lon = sq_diff_lon.argmin()


# Creating an empty pandas dataframe

df = pd.DataFrame(0, columns = ['O3'], index = time_data)


dt = np.arange(0, data2.variables['Time'].size)

for time_index in dt:
    df.iloc[time_index] = NO2[time_index, min_index_lat, min_index_lon]
    






















