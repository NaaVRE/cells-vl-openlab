
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--aerosol_variables', action='store', type=str, required=True, dest='aerosol_variables')


args = arg_parser.parse_args()
print(args)

id = args.id

aerosol_variables = json.loads(args.aerosol_variables)



variable_list = ""
for variable in aerosol_variables: 
    variable_list += '"' +  variable + '",'
variable_list = variable_list[:-1]
observed_properties = variable_list

file_observed_properties = open("/tmp/observed_properties_" + id + ".json", "w")
file_observed_properties.write(json.dumps(observed_properties))
file_observed_properties.close()
