
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




raw_data = []

file_raw_data = open("/tmp/raw_data_" + id + ".json", "w")
file_raw_data.write(json.dumps(raw_data))
file_raw_data.close()
