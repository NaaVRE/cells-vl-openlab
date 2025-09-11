
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--location_BNLplus_map', action='store', type=str, required=True, dest='location_BNLplus_map')

arg_parser.add_argument('--location_LUT_BNL2ET', action='store', type=str, required=True, dest='location_LUT_BNL2ET')


args = arg_parser.parse_args()
print(args)

id = args.id

location_BNLplus_map = args.location_BNLplus_map.replace('"','')
location_LUT_BNL2ET = args.location_LUT_BNL2ET.replace('"','')





file_location_ET_map = open("/tmp/location_ET_map_" + id + ".json", "w")
file_location_ET_map.write(json.dumps(location_ET_map))
file_location_ET_map.close()
