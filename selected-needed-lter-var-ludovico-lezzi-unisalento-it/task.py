
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--cleanedData', action='store', type=str, required=True, dest='cleanedData')


args = arg_parser.parse_args()
print(args)

id = args.id

cleanedData = json.loads(args.cleanedData)



selectedData = []
for name in cleanedData:
    selectedData.append(f"Hello, {name}!")

file_selectedData = open("/tmp/selectedData_" + id + ".json", "w")
file_selectedData.write(json.dumps(selectedData))
file_selectedData.close()
