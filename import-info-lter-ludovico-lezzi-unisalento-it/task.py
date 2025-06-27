
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




url = 'string'
data_vec = ["Alice", "Bob"]

file_data_vec = open("/tmp/data_vec_" + id + ".json", "w")
file_data_vec.write(json.dumps(data_vec))
file_data_vec.close()
