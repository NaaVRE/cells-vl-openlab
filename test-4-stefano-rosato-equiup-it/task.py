
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--test_list', action='store', type=str, required=True, dest='test_list')


args = arg_parser.parse_args()
print(args)

id = args.id

test_list = json.loads(args.test_list)



for item in test_list:
    print(item)

