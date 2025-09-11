
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--model_results', action='store', type=str, required=True, dest='model_results')


args = arg_parser.parse_args()
print(args)

id = args.id

model_results = json.loads(args.model_results)



print(model_results)

