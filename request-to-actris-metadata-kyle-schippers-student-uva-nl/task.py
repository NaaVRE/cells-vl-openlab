import requests

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--observed_properties', action='store', type=str, required=True, dest='observed_properties')

arg_parser.add_argument('--param_east_bound_longitude', action='store', type=float, required=True, dest='param_east_bound_longitude')
arg_parser.add_argument('--param_end_time', action='store', type=str, required=True, dest='param_end_time')
arg_parser.add_argument('--param_north_bound_latitude', action='store', type=float, required=True, dest='param_north_bound_latitude')
arg_parser.add_argument('--param_south_bound_latitude', action='store', type=float, required=True, dest='param_south_bound_latitude')
arg_parser.add_argument('--param_start_time', action='store', type=str, required=True, dest='param_start_time')
arg_parser.add_argument('--param_west_bound_longitude', action='store', type=float, required=True, dest='param_west_bound_longitude')

args = arg_parser.parse_args()
print(args)

id = args.id

observed_properties = args.observed_properties.replace('"','')

param_east_bound_longitude = args.param_east_bound_longitude
param_end_time = args.param_end_time.replace('"','')
param_north_bound_latitude = args.param_north_bound_latitude
param_south_bound_latitude = args.param_south_bound_latitude
param_start_time = args.param_start_time.replace('"','')
param_west_bound_longitude = args.param_west_bound_longitude


url = "https://prod-actris-md2.nilu.no/metadata/query/envri"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

counter = 0

metadata_list = []

while True:

    payload = ('{"time_range": ["' + param_start_time + '", "' + param_end_time + '"],' + 
           '"bounding_box": {"west_bound_longitude":' + str(param_west_bound_longitude) + ',' + 
           '"east_bound_longitude":' + str(param_east_bound_longitude) + ',' + 
           '"south_bound_latitude":' + str(param_south_bound_latitude) + ',' + 
           '"north_bound_latitude":' + str(param_north_bound_latitude) + '},' + 
           '"variables": [' + observed_properties + '],' +
           '"page":' + str(counter) + '}')
    
    response = requests.post(url, headers=headers, data=payload.encode("utf-8"))

    try:
        metadata_list.extend(response.json())
    except ValueError:
        print("Non-JSON response:", response.text)

    if response.status_code != 200 or not response.json(): 
        break
        
    print('Response Status: ' + str(response.status_code) + ' - Response Status: ' + response.reason + ' - Page: ' + str(counter) )
    counter+=1

print("Number of metadata elements retrieved: " + str(len(metadata_list)))
print(metadata_list)

file_metadata_list = open("/tmp/metadata_list_" + id + ".json", "w")
file_metadata_list.write(json.dumps(metadata_list))
file_metadata_list.close()
