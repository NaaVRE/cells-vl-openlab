import requests

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
code = r.status_code
print(code)

file_code = open("/tmp/code_" + id + ".json", "w")
file_code.write(json.dumps(code))
file_code.close()
