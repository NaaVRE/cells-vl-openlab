
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--traindata', action='store', type=str, required=True, dest='traindata')


args = arg_parser.parse_args()
print(args)

id = args.id

traindata = args.traindata.replace('"','')



print (traindata)


classfication=""

file_classfication = open("/tmp/classfication_" + id + ".json", "w")
file_classfication.write(json.dumps(classfication))
file_classfication.close()
