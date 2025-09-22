
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--mapdata', action='store', type=str, required=True, dest='mapdata')

arg_parser.add_argument('--scenario', action='store', type=str, required=True, dest='scenario')

arg_parser.add_argument('--sensordata', action='store', type=str, required=True, dest='sensordata')


args = arg_parser.parse_args()
print(args)

id = args.id

mapdata = args.mapdata.replace('"','')
scenario = args.scenario.replace('"','')
sensordata = args.sensordata.replace('"','')



print (mapdata)
print (sensordata)
print (scenario)

