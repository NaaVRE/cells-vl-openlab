
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
Humidity=""

file_Humidity = open("/tmp/Humidity_" + id + ".json", "w")
file_Humidity.write(json.dumps(Humidity))
file_Humidity.close()
file_Temperature = open("/tmp/Temperature_" + id + ".json", "w")
file_Temperature.write(json.dumps(Temperature))
file_Temperature.close()
file_Wind = open("/tmp/Wind_" + id + ".json", "w")
file_Wind.write(json.dumps(Wind))
file_Wind.close()
