import requests

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--api_url', action='store', type=str, required=True, dest='api_url')

arg_parser.add_argument('--param_search_term', action='store', type=str, required=True, dest='param_search_term')

args = arg_parser.parse_args()
print(args)

id = args.id

api_url = args.api_url.replace('"','')

param_search_term = args.param_search_term.replace('"','')


response_search_filtered = requests.get(api_url + "/resources/search?q=" + urllib.parse.quote(param_search_term.encode('utf8')) + "&facets=false")
filtered_data = response_search_filtered.json()
filtered_data

details_sealevel_result = requests.get(api_url + '/resources/details/' + filtered_data['results']['distributions'][0]['id'])
json_sealevel_result = details_sealevel_result.json()
json_sealevel_result

for available_format in json_sealevel_result['availableFormats']:
    if available_format['originalFormat'] == 'image/png':
            base_url = available_format['href']

service_parameters = json_sealevel_result['serviceParameters']

for parameter in service_parameters:
    if parameter['name'] == 'layers':
        layer = parameter['defaultValue']
    if 'property' in parameter:
        if parameter['property'] == 'epos:easternmostLongitude':
            maxlong = parameter['defaultValue']
        if parameter['property'] == 'epos:southernmostLatitude':
            minlat = parameter['defaultValue']
        if parameter['property'] == 'epos:northernmostLatitude':
            maxlat = parameter['defaultValue']
        if parameter['property'] == 'epos:westernmostLongitude':
            minlong = parameter['defaultValue']

file_base_url = open("/tmp/base_url_" + id + ".json", "w")
file_base_url.write(json.dumps(base_url))
file_base_url.close()
file_layer = open("/tmp/layer_" + id + ".json", "w")
file_layer.write(json.dumps(layer))
file_layer.close()
file_maxlat = open("/tmp/maxlat_" + id + ".json", "w")
file_maxlat.write(json.dumps(maxlat))
file_maxlat.close()
file_maxlong = open("/tmp/maxlong_" + id + ".json", "w")
file_maxlong.write(json.dumps(maxlong))
file_maxlong.close()
file_minlat = open("/tmp/minlat_" + id + ".json", "w")
file_minlat.write(json.dumps(minlat))
file_minlat.close()
file_minlong = open("/tmp/minlong_" + id + ".json", "w")
file_minlong.write(json.dumps(minlong))
file_minlong.close()
