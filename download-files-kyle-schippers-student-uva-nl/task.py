import os
import json
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


downloaded_filenames = []  

if param_protocol == 'opendap': 
    pass  
elif param_protocol == 'http': 
    if not os.path.exists("static/actrisexv"):
        os.makedirs("static/actrisexv")

    for element in metadata_list: 
        r = requests.get(element['md_distribution_information'][0]['dataset_url'])
        filename = "ACTRIS_" + element['md_metadata']['file_identifier']
        downloaded_filenames.append(filename)  # save for later
        print(filename)

        filepath = os.path.join("static/actrisexv", filename)  #
        with open(filepath, mode="wb") as file:
            file.write(r.content)

else: 
    print('Please choose a valid protocol: http or opendap')

run_id = os.getenv("RUN_ID", "localtest")

if downloaded_filenames:
    filename_to_save = downloaded_filenames[-1]
else:
    filename_to_save = None  

with open(f"/tmp/filename_{run_id}.json", "w") as file_filename:
    json.dump(filename_to_save, file_filename)

file_filename = open("/tmp/filename_" + id + ".json", "w")
file_filename.write(json.dumps(filename))
file_filename.close()
