
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--remoteSensoringURL', action='store', type=str, required=True, dest='remoteSensoringURL')


args = arg_parser.parse_args()
print(args)

id = args.id

remoteSensoringURL = args.remoteSensoringURL.replace('"','')



print (remoteSensoringURL)

mapv=""
raster=""

file_mapv = open("/tmp/mapv_" + id + ".json", "w")
file_mapv.write(json.dumps(mapv))
file_mapv.close()
file_raster = open("/tmp/raster_" + id + ".json", "w")
file_raster.write(json.dumps(raster))
file_raster.close()
