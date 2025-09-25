
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
LU=""
LAI=""
NDVI=""

file_LAI = open("/tmp/LAI_" + id + ".json", "w")
file_LAI.write(json.dumps(LAI))
file_LAI.close()
file_LU = open("/tmp/LU_" + id + ".json", "w")
file_LU.write(json.dumps(LU))
file_LU.close()
file_NDVI = open("/tmp/NDVI_" + id + ".json", "w")
file_NDVI.write(json.dumps(NDVI))
file_NDVI.close()
file_mapv = open("/tmp/mapv_" + id + ".json", "w")
file_mapv.write(json.dumps(mapv))
file_mapv.close()
file_raster = open("/tmp/raster_" + id + ".json", "w")
file_raster.write(json.dumps(raster))
file_raster.close()
