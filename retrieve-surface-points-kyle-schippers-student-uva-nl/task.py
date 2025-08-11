
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--ds', action='store', type=str, required=True, dest='ds')


args = arg_parser.parse_args()
print(args)

id = args.id

ds = json.loads(args.ds)



dsargo=ds.argo.point2profile()
dsargo_surf=dsargo.isel(N_LEVELS=0)

file_dsargo_surf = open("/tmp/dsargo_surf_" + id + ".json", "w")
file_dsargo_surf.write(json.dumps(dsargo_surf))
file_dsargo_surf.close()
