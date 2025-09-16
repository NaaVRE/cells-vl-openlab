
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--data_', action='store', type=str, required=True, dest='data_')


args = arg_parser.parse_args()
print(args)

id = args.id

data_ = json.loads(args.data_)



new_data = data_
data_to_append = ["Nablo", "Bablo"]
for item in data_to_append:
   new_data.append(item) 
data_ = new_data

file_data_ = open("/tmp/data__" + id + ".json", "w")
file_data_.write(json.dumps(data_))
file_data_.close()
