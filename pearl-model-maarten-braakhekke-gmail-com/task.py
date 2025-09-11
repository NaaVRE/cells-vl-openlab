
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--bulk_density', action='store', type=str, required=True, dest='bulk_density')

arg_parser.add_argument('--cell_id', action='store', type=int, required=True, dest='cell_id')

arg_parser.add_argument('--clay_frac', action='store', type=str, required=True, dest='clay_frac')

arg_parser.add_argument('--OM_frac', action='store', type=str, required=True, dest='OM_frac')

arg_parser.add_argument('--ph_h2o', action='store', type=str, required=True, dest='ph_h2o')

arg_parser.add_argument('--sand_frac', action='store', type=str, required=True, dest='sand_frac')

arg_parser.add_argument('--silt_frac', action='store', type=str, required=True, dest='silt_frac')


args = arg_parser.parse_args()
print(args)

id = args.id

bulk_density = json.loads(args.bulk_density)
cell_id = args.cell_id
clay_frac = json.loads(args.clay_frac)
OM_frac = json.loads(args.OM_frac)
ph_h2o = json.loads(args.ph_h2o)
sand_frac = json.loads(args.sand_frac)
silt_frac = json.loads(args.silt_frac)





file_pec = open("/tmp/pec_" + id + ".json", "w")
file_pec.write(json.dumps(pec))
file_pec.close()
