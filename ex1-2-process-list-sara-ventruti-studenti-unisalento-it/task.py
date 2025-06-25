
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_password = os.getenv('secret_password')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--names', action='store', type=str, required=True, dest='names')

arg_parser.add_argument('--param_greeting', action='store', type=str, required=True, dest='param_greeting')

args = arg_parser.parse_args()
print(args)

id = args.id

names = json.loads(args.names)

print(args.param_greeting)
print(type(args.param_greeting))
try:
    param_greeting = json.loads(args.param_greeting)
except Exception as e:
    if e.__class__.__name__ == 'JSONDecodeError':
        import ast
        param_greeting = ast.literal_eval(args.param_greeting.replace('[','["').replace(',','","').replace('" ','"').replace(']','"]').replace("'",""))
    else:
        raise e


for name in names:
    print(f"{param_greeting}, {name}! The password is: {secret_password}")

