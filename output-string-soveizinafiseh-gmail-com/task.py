
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--my_input', action='store', type=str, required=True, dest='my_input')


args = arg_parser.parse_args()
print(args)

id = args.id

my_input = args.my_input.replace('"','')



print(my_input)

