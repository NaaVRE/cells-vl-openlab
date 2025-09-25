
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




Temperature=""
Wind=""
Himidity=""

file_Himidity = open("/tmp/Himidity_" + id + ".json", "w")
file_Himidity.write(json.dumps(Himidity))
file_Himidity.close()
file_Temperature = open("/tmp/Temperature_" + id + ".json", "w")
file_Temperature.write(json.dumps(Temperature))
file_Temperature.close()
file_Wind = open("/tmp/Wind_" + id + ".json", "w")
file_Wind.write(json.dumps(Wind))
file_Wind.close()
