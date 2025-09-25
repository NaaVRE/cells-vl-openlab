
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--input_1', action='store', type=str, required=True, dest='input_1')

arg_parser.add_argument('--input_2', action='store', type=str, required=True, dest='input_2')


args = arg_parser.parse_args()
print(args)

id = args.id

input_1 = args.input_1.replace('"','')
input_2 = args.input_2.replace('"','')



print(input_1)
print(input_2)


output_1 = "An output variable"
output_2 = "Another output variable"

file_output_1 = open("/tmp/output_1_" + id + ".json", "w")
file_output_1.write(json.dumps(output_1))
file_output_1.close()
file_output_2 = open("/tmp/output_2_" + id + ".json", "w")
file_output_2.write(json.dumps(output_2))
file_output_2.close()
