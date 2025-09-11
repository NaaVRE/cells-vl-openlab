
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--detailed_table_path', action='store', type=str, required=True, dest='detailed_table_path')


args = arg_parser.parse_args()
print(args)

id = args.id

detailed_table_path = args.detailed_table_path.replace('"','')





file_summary_table_path = open("/tmp/summary_table_path_" + id + ".json", "w")
file_summary_table_path.write(json.dumps(summary_table_path))
file_summary_table_path.close()
