import os
import numpy

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()
print(args)

id = args.id



conf_data_path = conf_data_path = '/tmp/data'

numbers = numpy.random.normal(size=100_000)

data_file = os.path.join(conf_data_path, "ex3-data.out")
os.makedirs(conf_data_path, exist_ok=True)
numpy.savetxt(data_file, numbers)

file_data_file = open("/tmp/data_file_" + id + ".json", "w")
file_data_file.write(json.dumps(data_file))
file_data_file.close()
