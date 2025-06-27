
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--BioindexesTable', action='store', type=str, required=True, dest='BioindexesTable')

arg_parser.add_argument('--selectedData', action='store', type=str, required=True, dest='selectedData')


args = arg_parser.parse_args()
print(args)

id = args.id

BioindexesTable = json.loads(args.BioindexesTable)
selectedData = json.loads(args.selectedData)



for name in BioindexesTable:
    BioindexesTable.append(f"Hello, {name}!")
for name in selectedData:
    BioindexesTable.append(f"Hello, {name}!")

