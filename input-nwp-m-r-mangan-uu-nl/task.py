
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--NWP', action='store', type=str, required=True, dest='NWP')


args = arg_parser.parse_args()
print(args)

id = args.id

NWP = args.NWP.replace('"','')



print(NWP)

u = ""
T = ""
q = ""

file_T = open("/tmp/T_" + id + ".json", "w")
file_T.write(json.dumps(T))
file_T.close()
file_q = open("/tmp/q_" + id + ".json", "w")
file_q.write(json.dumps(q))
file_q.close()
file_u = open("/tmp/u_" + id + ".json", "w")
file_u.write(json.dumps(u))
file_u.close()
