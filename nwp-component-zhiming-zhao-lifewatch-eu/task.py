
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--InputURL', action='store', type=str, required=True, dest='InputURL')


args = arg_parser.parse_args()
print(args)

id = args.id

InputURL = args.InputURL.replace('"','')



print (InputURL)
U=""
Ta=""
Q=""

file_Q = open("/tmp/Q_" + id + ".json", "w")
file_Q.write(json.dumps(Q))
file_Q.close()
file_Ta = open("/tmp/Ta_" + id + ".json", "w")
file_Ta.write(json.dumps(Ta))
file_Ta.close()
file_U = open("/tmp/U_" + id + ".json", "w")
file_U.write(json.dumps(U))
file_U.close()
