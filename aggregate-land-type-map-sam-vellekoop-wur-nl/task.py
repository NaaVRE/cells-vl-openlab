
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--vegetation_structure_raster_path', action='store', type=str, required=True, dest='vegetation_structure_raster_path')


args = arg_parser.parse_args()
print(args)

id = args.id

vegetation_structure_raster_path = args.vegetation_structure_raster_path.replace('"','')





file_aggregated_land_types_dir = open("/tmp/aggregated_land_types_dir_" + id + ".json", "w")
file_aggregated_land_types_dir.write(json.dumps(aggregated_land_types_dir))
file_aggregated_land_types_dir.close()
