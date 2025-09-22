
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--InputOfTheSkeletonCell', action='store', type=str, required=True, dest='InputOfTheSkeletonCell')


args = arg_parser.parse_args()
print(args)

id = args.id

InputOfTheSkeletonCell = args.InputOfTheSkeletonCell.replace('"','')



print (InputOfTheSkeletonCell)

OutputOfTheSkeletonCell="test"

file_OutputOfTheSkeletonCell = open("/tmp/OutputOfTheSkeletonCell_" + id + ".json", "w")
file_OutputOfTheSkeletonCell.write(json.dumps(OutputOfTheSkeletonCell))
file_OutputOfTheSkeletonCell.close()
