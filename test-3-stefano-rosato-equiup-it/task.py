
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




test_list = ['uno', 'due']

file_test_list = open("/tmp/test_list_" + id + ".json", "w")
file_test_list.write(json.dumps(test_list))
file_test_list.close()
