
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--model_parameters', action='store', type=str, required=True, dest='model_parameters')

arg_parser.add_argument('--preprocessed_data', action='store', type=str, required=True, dest='preprocessed_data')

arg_parser.add_argument('--testrun_success', action='store', type=int, required=True, dest='testrun_success')


args = arg_parser.parse_args()
print(args)

id = args.id

model_parameters = json.loads(args.model_parameters)
preprocessed_data = json.loads(args.preprocessed_data)
testrun_success = args.testrun_success



print(testrun_success)

model_results = preprocessed_data
print(model_parameters)

file_model_results = open("/tmp/model_results_" + id + ".json", "w")
file_model_results.write(json.dumps(model_results))
file_model_results.close()
