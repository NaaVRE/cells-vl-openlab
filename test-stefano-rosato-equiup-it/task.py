
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id




test_var=10

file_test_var = open("/tmp/test_var_" + id + ".json", "w")
file_test_var.write(json.dumps(test_var))
file_test_var.close()
