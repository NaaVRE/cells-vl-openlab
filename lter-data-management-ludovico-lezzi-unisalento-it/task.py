
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--data', action='store', type=str, required=True, dest='data')


args = arg_parser.parse_args()
print(args)

id = args.id

data = json.loads(args.data)



cleanedData = []
for name in data:
    cleanedData.append(f"Hello, {name}!")

file_cleanedData = open("/tmp/cleanedData_" + id + ".json", "w")
file_cleanedData.write(json.dumps(cleanedData))
file_cleanedData.close()
