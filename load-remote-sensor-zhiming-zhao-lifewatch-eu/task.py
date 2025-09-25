
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
remoteSensorData=""

file_remoteSensorData = open("/tmp/remoteSensorData_" + id + ".json", "w")
file_remoteSensorData.write(json.dumps(remoteSensorData))
file_remoteSensorData.close()
