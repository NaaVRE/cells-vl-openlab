from minio import Minio

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_minio_access_key = os.getenv('secret_minio_access_key')
secret_minio_secret_key = os.getenv('secret_minio_secret_key')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_minio_endpoint', action='store', type=str, required=True, dest='param_minio_endpoint')
arg_parser.add_argument('--param_minio_user_prefix', action='store', type=str, required=True, dest='param_minio_user_prefix')

args = arg_parser.parse_args()
print(args)

id = args.id


param_minio_endpoint = args.param_minio_endpoint.replace('"','')
param_minio_user_prefix = args.param_minio_user_prefix.replace('"','')


mc = Minio(endpoint=param_minio_endpoint,
           access_key=secret_minio_access_key,
           secret_key=secret_minio_secret_key)


file="/tmp/data/ant_coordinates.csv"
mc.fget_object(bucket_name="naa-vre-user-data", object_name=f"{param_minio_user_prefix}/datafile/ant_coordinates.csv", file_path=file)

file_file = open("/tmp/file_" + id + ".json", "w")
file_file.write(json.dumps(file))
file_file.close()
