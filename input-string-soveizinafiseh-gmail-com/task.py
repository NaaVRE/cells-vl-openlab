
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




my_input = "Hello, this is me"

file_my_input = open("/tmp/my_input_" + id + ".json", "w")
file_my_input.write(json.dumps(my_input))
file_my_input.close()
