
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--gvg_raster_path', action='store', type=str, required=True, dest='gvg_raster_path')

arg_parser.add_argument('--gvg_suitabilities_path', action='store', type=str, required=True, dest='gvg_suitabilities_path')

arg_parser.add_argument('--ndep_raster_path', action='store', type=str, required=True, dest='ndep_raster_path')

arg_parser.add_argument('--ndep_suitabilities_path', action='store', type=str, required=True, dest='ndep_suitabilities_path')

arg_parser.add_argument('--ph_raster_path', action='store', type=str, required=True, dest='ph_raster_path')

arg_parser.add_argument('--ph_suitabilities_path', action='store', type=str, required=True, dest='ph_suitabilities_path')

arg_parser.add_argument('--species_traits_path', action='store', type=str, required=True, dest='species_traits_path')


args = arg_parser.parse_args()
print(args)

id = args.id

gvg_raster_path = args.gvg_raster_path.replace('"','')
gvg_suitabilities_path = args.gvg_suitabilities_path.replace('"','')
ndep_raster_path = args.ndep_raster_path.replace('"','')
ndep_suitabilities_path = args.ndep_suitabilities_path.replace('"','')
ph_raster_path = args.ph_raster_path.replace('"','')
ph_suitabilities_path = args.ph_suitabilities_path.replace('"','')
species_traits_path = args.species_traits_path.replace('"','')





file_environmental_factor_dir = open("/tmp/environmental_factor_dir_" + id + ".json", "w")
file_environmental_factor_dir.write(json.dumps(environmental_factor_dir))
file_environmental_factor_dir.close()
