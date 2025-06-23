
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--test_var', action='store', type=int, required=True, dest='test_var')


args = arg_parser.parse_args()
print(args)

id = args.id

test_var = args.test_var



add=test_var+1

