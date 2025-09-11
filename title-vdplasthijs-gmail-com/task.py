
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--my_input1', action='store', type=str, required=True, dest='my_input1')


args = arg_parser.parse_args()
print(args)

id = args.id

my_input1 = args.my_input1.replace('"','')





file_my_output1 = open("/tmp/my_output1_" + id + ".json", "w")
file_my_output1.write(json.dumps(my_output1))
file_my_output1.close()
file_my_output2 = open("/tmp/my_output2_" + id + ".json", "w")
file_my_output2.write(json.dumps(my_output2))
file_my_output2.close()
file_my_output3 = open("/tmp/my_output3_" + id + ".json", "w")
file_my_output3.write(json.dumps(my_output3))
file_my_output3.close()
