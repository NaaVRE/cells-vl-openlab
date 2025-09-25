
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--MapV', action='store', type=str, required=True, dest='MapV')

arg_parser.add_argument('--RasterData', action='store', type=str, required=True, dest='RasterData')

arg_parser.add_argument('--Timeseriesoffarm', action='store', type=str, required=True, dest='Timeseriesoffarm')


args = arg_parser.parse_args()
print(args)

id = args.id

MapV = args.MapV.replace('"','')
RasterData = args.RasterData.replace('"','')
Timeseriesoffarm = args.Timeseriesoffarm.replace('"','')



ET=""

print (RasterData)
print (MapV)
print (Timeseriesoffarm)

file_ET = open("/tmp/ET_" + id + ".json", "w")
file_ET.write(json.dumps(ET))
file_ET.close()
