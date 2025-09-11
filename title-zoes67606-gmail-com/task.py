
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--my_input', action='store', type=str, required=True, dest='my_input')

arg_parser.add_argument('--my_other_input', action='store', type=int, required=True, dest='my_other_input')


args = arg_parser.parse_args()
print(args)

id = args.id

my_input = args.my_input.replace('"','')
my_other_input = args.my_other_input





file_my_other_output = open("/tmp/my_other_output_" + id + ".json", "w")
file_my_other_output.write(json.dumps(my_other_output))
file_my_other_output.close()
file_my_output = open("/tmp/my_output_" + id + ".json", "w")
file_my_output.write(json.dumps(my_output))
file_my_output.close()
