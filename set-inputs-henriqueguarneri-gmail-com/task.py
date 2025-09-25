
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




input_1 = "An input variable"
input_2 = "Another input variable"

file_input_1 = open("/tmp/input_1_" + id + ".json", "w")
file_input_1.write(json.dumps(input_1))
file_input_1.close()
file_input_2 = open("/tmp/input_2_" + id + ".json", "w")
file_input_2.write(json.dumps(input_2))
file_input_2.close()
