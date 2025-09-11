
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--raw_data', action='store', type=str, required=True, dest='raw_data')


args = arg_parser.parse_args()
print(args)

id = args.id

raw_data = json.loads(args.raw_data)



preprocessed_data = raw_data

file_preprocessed_data = open("/tmp/preprocessed_data_" + id + ".json", "w")
file_preprocessed_data.write(json.dumps(preprocessed_data))
file_preprocessed_data.close()
