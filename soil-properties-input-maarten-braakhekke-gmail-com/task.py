
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_OM_frac = open("/tmp/OM_frac_" + id + ".json", "w")
file_OM_frac.write(json.dumps(OM_frac))
file_OM_frac.close()
file_bulk_density = open("/tmp/bulk_density_" + id + ".json", "w")
file_bulk_density.write(json.dumps(bulk_density))
file_bulk_density.close()
file_cell_id = open("/tmp/cell_id_" + id + ".json", "w")
file_cell_id.write(json.dumps(cell_id))
file_cell_id.close()
file_clay_frac = open("/tmp/clay_frac_" + id + ".json", "w")
file_clay_frac.write(json.dumps(clay_frac))
file_clay_frac.close()
file_ph_h2o = open("/tmp/ph_h2o_" + id + ".json", "w")
file_ph_h2o.write(json.dumps(ph_h2o))
file_ph_h2o.close()
file_sand_frac = open("/tmp/sand_frac_" + id + ".json", "w")
file_sand_frac.write(json.dumps(sand_frac))
file_sand_frac.close()
file_silt_frac = open("/tmp/silt_frac_" + id + ".json", "w")
file_silt_frac.write(json.dumps(silt_frac))
file_silt_frac.close()
