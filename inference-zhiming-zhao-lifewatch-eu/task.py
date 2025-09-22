
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--inputd', action='store', type=str, required=True, dest='inputd')

arg_parser.add_argument('--weight', action='store', type=str, required=True, dest='weight')


args = arg_parser.parse_args()
print(args)

id = args.id

inputd = args.inputd.replace('"','')
weight = args.weight.replace('"','')



print (weight)
print (inputd)

result=""

file_result = open("/tmp/result_" + id + ".json", "w")
file_result.write(json.dumps(result))
file_result.close()
