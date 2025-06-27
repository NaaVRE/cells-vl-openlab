
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--data_vec', action='store', type=str, required=True, dest='data_vec')


args = arg_parser.parse_args()
print(args)

id = args.id

data_vec = json.loads(args.data_vec)



data = []
for name in data_vec:
    data.append(f"Hello, {name}!")

file_data = open("/tmp/data_" + id + ".json", "w")
file_data.write(json.dumps(data))
file_data.close()
