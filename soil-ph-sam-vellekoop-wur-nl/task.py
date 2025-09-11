
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_ph_raster_path = open("/tmp/ph_raster_path_" + id + ".json", "w")
file_ph_raster_path.write(json.dumps(ph_raster_path))
file_ph_raster_path.close()
