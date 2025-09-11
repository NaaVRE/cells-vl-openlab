
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--model_parameters', action='store', type=str, required=True, dest='model_parameters')


args = arg_parser.parse_args()
print(args)

id = args.id

model_parameters = json.loads(args.model_parameters)



if model_parameters:
    testrun_success = 1
else:
    testrun_success = 0

file_testrun_success = open("/tmp/testrun_success_" + id + ".json", "w")
file_testrun_success.write(json.dumps(testrun_success))
file_testrun_success.close()
