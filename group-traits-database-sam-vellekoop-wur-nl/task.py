
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id






file_group_traits_path = open("/tmp/group_traits_path_" + id + ".json", "w")
file_group_traits_path.write(json.dumps(group_traits_path))
file_group_traits_path.close()
