import argopy
from argopy import DataFetcher

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


argopy.set_options(src=param_src,ds='phy',mode='standard')
f=DataFetcher().region([param_lon_west,param_lon_east,param_lat_south,param_lat_north,param_depth_min,param_depth_max,param_date_min,param_date_max])
print(f)
ds=f.to_xarray()
print(ds)

file_ds = open("/tmp/ds_" + id + ".json", "w")
file_ds.write(json.dumps(ds))
file_ds.close()
