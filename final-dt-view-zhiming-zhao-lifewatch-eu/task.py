
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--ET', action='store', type=str, required=True, dest='ET')


args = arg_parser.parse_args()
print(args)

id = args.id

ET = args.ET.replace('"','')



print (ET)
RasterData=""
MapV=""
Timeseriesoffarm=""

file_MapV = open("/tmp/MapV_" + id + ".json", "w")
file_MapV.write(json.dumps(MapV))
file_MapV.close()
file_RasterData = open("/tmp/RasterData_" + id + ".json", "w")
file_RasterData.write(json.dumps(RasterData))
file_RasterData.close()
file_Timeseriesoffarm = open("/tmp/Timeseriesoffarm_" + id + ".json", "w")
file_Timeseriesoffarm.write(json.dumps(Timeseriesoffarm))
file_Timeseriesoffarm.close()
