
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--lai', action='store', type=str, required=True, dest='lai')

arg_parser.add_argument('--lu', action='store', type=str, required=True, dest='lu')

arg_parser.add_argument('--ndvi', action='store', type=str, required=True, dest='ndvi')

arg_parser.add_argument('--q', action='store', type=str, required=True, dest='q')

arg_parser.add_argument('--qs', action='store', type=str, required=True, dest='qs')

arg_parser.add_argument('--T', action='store', type=str, required=True, dest='T')

arg_parser.add_argument('--Ts', action='store', type=str, required=True, dest='Ts')

arg_parser.add_argument('--u', action='store', type=str, required=True, dest='u')

arg_parser.add_argument('--us', action='store', type=str, required=True, dest='us')


args = arg_parser.parse_args()
print(args)

id = args.id

lai = args.lai.replace('"','')
lu = args.lu.replace('"','')
ndvi = args.ndvi.replace('"','')
q = args.q.replace('"','')
qs = args.qs.replace('"','')
T = args.T.replace('"','')
Ts = args.Ts.replace('"','')
u = args.u.replace('"','')
us = args.us.replace('"','')



print(ndvi, lai, lu, Ts, qs, us, u, T, q)

et = ""

file_et = open("/tmp/et_" + id + ".json", "w")
file_et.write(json.dumps(et))
file_et.close()
