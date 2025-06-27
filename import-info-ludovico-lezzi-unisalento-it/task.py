
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--url', action='store', type=str, required=True, dest='url')


args = arg_parser.parse_args()
print(args)

id = args.id

url = args.url.replace('"','')



url

data_vec = 1 + url

file_data_vec = open("/tmp/data_vec_" + id + ".json", "w")
file_data_vec.write(json.dumps(data_vec))
file_data_vec.close()
