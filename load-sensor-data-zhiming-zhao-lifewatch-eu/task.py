
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--sensorurl', action='store', type=str, required=True, dest='sensorurl')


args = arg_parser.parse_args()
print(args)

id = args.id

sensorurl = args.sensorurl.replace('"','')



print (sensorurl)


sensordata=""

file_sensordata = open("/tmp/sensordata_" + id + ".json", "w")
file_sensordata.write(json.dumps(sensordata))
file_sensordata.close()
