
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--datasource1', action='store', type=str, required=True, dest='datasource1')

arg_parser.add_argument('--datasource2', action='store', type=str, required=True, dest='datasource2')


args = arg_parser.parse_args()
print(args)

id = args.id

datasource1 = args.datasource1.replace('"','')
datasource2 = args.datasource2.replace('"','')



print (datasource1)
print (datasource2)


dataoutputI=""

file_dataoutputI = open("/tmp/dataoutputI_" + id + ".json", "w")
file_dataoutputI.write(json.dumps(dataoutputI))
file_dataoutputI.close()
