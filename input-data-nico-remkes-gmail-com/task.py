
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




variable1 = 23
variable2 = 22

file_variable1 = open("/tmp/variable1_" + id + ".json", "w")
file_variable1.write(json.dumps(variable1))
file_variable1.close()
file_variable2 = open("/tmp/variable2_" + id + ".json", "w")
file_variable2.write(json.dumps(variable2))
file_variable2.close()
