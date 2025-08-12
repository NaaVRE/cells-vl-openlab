import os
import requests

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--metadata_list', action='store', type=str, required=True, dest='metadata_list')

arg_parser.add_argument('--param_protocol', action='store', type=str, required=True, dest='param_protocol')

args = arg_parser.parse_args()
print(args)

id = args.id

metadata_list = json.loads(args.metadata_list)

param_protocol = args.param_protocol.replace('"','')


if param_protocol == 'opendap': 
    next
elif param_protocol == 'http': 
    if not os.path.exists("static/actrisexv"):
        os.makedirs("static/actrisexv")

    for element in metadata_list: 
        r = requests.get(element['md_distribution_information'][0]['dataset_url'])
        filename = "ACTRIS_"+element['md_metadata']['file_identifier']
        print(filename)
        filepath = os.path.join("static/actrisexv", filename)  # Specify the folder path
        with open(filepath, mode="wb") as file:
            file.write(r.content)
else: 
    print('Please choose a valid protocol: http or opendap')

file_filename = open("/tmp/filename_" + id + ".json", "w")
file_filename.write(json.dumps(filename))
file_filename.close()
