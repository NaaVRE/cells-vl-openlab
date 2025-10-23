
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




geospatial_shapefile = "the area to analyze"

file_geospatial_shapefile = open("/tmp/geospatial_shapefile_" + id + ".json", "w")
file_geospatial_shapefile.write(json.dumps(geospatial_shapefile))
file_geospatial_shapefile.close()
