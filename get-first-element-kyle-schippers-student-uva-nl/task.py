
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--metadata_list', action='store', type=str, required=True, dest='metadata_list')


args = arg_parser.parse_args()
print(args)

id = args.id

metadata_list = json.loads(args.metadata_list)



first_element = next(iter(metadata_list)) 

file_first_element = open("/tmp/first_element_" + id + ".json", "w")
file_first_element.write(json.dumps(first_element))
file_first_element.close()
