
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--in_situ', action='store', type=str, required=True, dest='in_situ')


args = arg_parser.parse_args()
print(args)

id = args.id

in_situ = args.in_situ.replace('"','')



print(in_situ)

us = ""
Ts = ""
qs = ""

file_Ts = open("/tmp/Ts_" + id + ".json", "w")
file_Ts.write(json.dumps(Ts))
file_Ts.close()
file_qs = open("/tmp/qs_" + id + ".json", "w")
file_qs.write(json.dumps(qs))
file_qs.close()
file_us = open("/tmp/us_" + id + ".json", "w")
file_us.write(json.dumps(us))
file_us.close()
