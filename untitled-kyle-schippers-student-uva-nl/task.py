import requests

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




api_url = 'https://www.ics-c.epos-eu.org/api/v1'

search_endpoint = f"{api_url}/resources/search?q=&facets=false"
response_search = requests.get(search_endpoint)
data = response_search.json()

file_api_url = open("/tmp/api_url_" + id + ".json", "w")
file_api_url.write(json.dumps(api_url))
file_api_url.close()
