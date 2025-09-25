
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--variable1', action='store', type=int, required=True, dest='variable1')

arg_parser.add_argument('--variable2', action='store', type=int, required=True, dest='variable2')


args = arg_parser.parse_args()
print(args)

id = args.id

variable1 = args.variable1
variable2 = args.variable2



variable3 = variable1
variable4= variable2

file_variable3 = open("/tmp/variable3_" + id + ".json", "w")
file_variable3.write(json.dumps(variable3))
file_variable3.close()
file_variable4 = open("/tmp/variable4_" + id + ".json", "w")
file_variable4.write(json.dumps(variable4))
file_variable4.close()
