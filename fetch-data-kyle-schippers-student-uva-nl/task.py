from argopy import DataFetcher
import numpy as np
from matplotlib import dates as mdates

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_date_max', action='store', type=str, required=True, dest='param_date_max')
arg_parser.add_argument('--param_date_min', action='store', type=str, required=True, dest='param_date_min')
arg_parser.add_argument('--param_depth_max', action='store', type=int, required=True, dest='param_depth_max')
arg_parser.add_argument('--param_depth_min', action='store', type=int, required=True, dest='param_depth_min')
arg_parser.add_argument('--param_lat_north', action='store', type=int, required=True, dest='param_lat_north')
arg_parser.add_argument('--param_lat_south', action='store', type=int, required=True, dest='param_lat_south')
arg_parser.add_argument('--param_lon_east', action='store', type=int, required=True, dest='param_lon_east')
arg_parser.add_argument('--param_lon_west', action='store', type=int, required=True, dest='param_lon_west')
arg_parser.add_argument('--param_src', action='store', type=str, required=True, dest='param_src')

args = arg_parser.parse_args()
print(args)

id = args.id


param_date_max = args.param_date_max.replace('"','')
param_date_min = args.param_date_min.replace('"','')
param_depth_max = args.param_depth_max
param_depth_min = args.param_depth_min
param_lat_north = args.param_lat_north
param_lat_south = args.param_lat_south
param_lon_east = args.param_lon_east
param_lon_west = args.param_lon_west
param_src = args.param_src.replace('"','')


argopy.set_options(src=param_src, ds='phy', mode='standard')
f = DataFetcher().region([
    param_lon_west, param_lon_east,
    param_lat_south, param_lat_north,
    param_depth_min, param_depth_max,
    param_date_min, param_date_max
])
ds = f.to_xarray()

dsargo = ds.argo.point2profile()
dsargo_surf = dsargo.isel(N_LEVELS=0)

longitudes              = dsargo_surf['LONGITUDE'].values.flatten().tolist()
latitudes               = dsargo_surf['LATITUDE'].values.flatten().tolist()
temperatures_spatial    = dsargo_surf['TEMP'].values.flatten().tolist()
temperatures_temporal   = temperatures_spatial[:]  # same data
_times_dt               = dsargo_surf['TIME'].values.astype('datetime64[ms]').astype('O').tolist()
times                   = mdates.date2num(_times_dt).tolist()

t_arr = ds['TEMP'].values
p_arr = ds['PRES'].values
mask  = np.isfinite(t_arr) & np.isfinite(p_arr)
temperatures_vertical = t_arr[mask].ravel().astype(float).tolist()
pressures_vertical    = (-p_arr[mask]).ravel().astype(float).tolist()

temp_long_name  = str(ds['TEMP'].attrs.get('long_name', 'Temperature'))
temp_units      = str(ds['TEMP'].attrs.get('units', ''))
title_temporal  = f"{temp_long_name} in {temp_units} at the surface betw. {param_date_min} and {param_date_max}"
title_spatial   = f"Sea-surface temperatures in C° betw. {param_date_min} and {param_date_max}"
title_vertical  = f"Sea subsurface temperatures in C° betw. {param_date_min} and {param_date_max}"

file_latitudes = open("/tmp/latitudes_" + id + ".json", "w")
file_latitudes.write(json.dumps(latitudes))
file_latitudes.close()
file_longitudes = open("/tmp/longitudes_" + id + ".json", "w")
file_longitudes.write(json.dumps(longitudes))
file_longitudes.close()
file_pressures_vertical = open("/tmp/pressures_vertical_" + id + ".json", "w")
file_pressures_vertical.write(json.dumps(pressures_vertical))
file_pressures_vertical.close()
file_temperatures_spatial = open("/tmp/temperatures_spatial_" + id + ".json", "w")
file_temperatures_spatial.write(json.dumps(temperatures_spatial))
file_temperatures_spatial.close()
file_temperatures_temporal = open("/tmp/temperatures_temporal_" + id + ".json", "w")
file_temperatures_temporal.write(json.dumps(temperatures_temporal))
file_temperatures_temporal.close()
file_temperatures_vertical = open("/tmp/temperatures_vertical_" + id + ".json", "w")
file_temperatures_vertical.write(json.dumps(temperatures_vertical))
file_temperatures_vertical.close()
file_times = open("/tmp/times_" + id + ".json", "w")
file_times.write(json.dumps(times))
file_times.close()
file_title_spatial = open("/tmp/title_spatial_" + id + ".json", "w")
file_title_spatial.write(json.dumps(title_spatial))
file_title_spatial.close()
file_title_temporal = open("/tmp/title_temporal_" + id + ".json", "w")
file_title_temporal.write(json.dumps(title_temporal))
file_title_temporal.close()
file_title_vertical = open("/tmp/title_vertical_" + id + ".json", "w")
file_title_vertical.write(json.dumps(title_vertical))
file_title_vertical.close()
