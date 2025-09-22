
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--datasource', action='store', type=str, required=True, dest='datasource')


args = arg_parser.parse_args()
print(args)

id = args.id

datasource = args.datasource.replace('"','')



print(datasource);



dataouput="data for DT"

file_dataouput = open("/tmp/dataouput_" + id + ".json", "w")
file_dataouput.write(json.dumps(dataouput))
file_dataouput.close()
