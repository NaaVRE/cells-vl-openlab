
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--model_A', action='store', type=str, required=True, dest='model_A')


args = arg_parser.parse_args()
print(args)

id = args.id

model_A = args.model_A.replace('"','')



print(model_A)

