
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_location_BNLplus_map = open("/tmp/location_BNLplus_map_" + id + ".json", "w")
file_location_BNLplus_map.write(json.dumps(location_BNLplus_map))
file_location_BNLplus_map.close()
