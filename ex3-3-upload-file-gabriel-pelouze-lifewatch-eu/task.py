from minio import Minio

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()

secret_minio_access_key = os.getenv('secret_minio_access_key')
secret_minio_secret_key = os.getenv('secret_minio_secret_key')

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--figure_file', action='store', type=str, required=True, dest='figure_file')

arg_parser.add_argument('--param_minio_bucket', action='store', type=str, required=True, dest='param_minio_bucket')
arg_parser.add_argument('--param_minio_endpoint', action='store', type=str, required=True, dest='param_minio_endpoint')
arg_parser.add_argument('--param_minio_user_prefix', action='store', type=str, required=True, dest='param_minio_user_prefix')

args = arg_parser.parse_args()
print(args)

id = args.id

figure_file = args.figure_file.replace('"','')

param_minio_bucket = args.param_minio_bucket.replace('"','')
param_minio_endpoint = args.param_minio_endpoint.replace('"','')
param_minio_user_prefix = args.param_minio_user_prefix.replace('"','')


mc = Minio(
    endpoint=param_minio_endpoint,
    access_key=secret_minio_access_key,
    secret_key=secret_minio_secret_key,
    )
mc.fput_object(
    bucket_name=param_minio_bucket,
    file_path=figure_file,
    object_name=f"{param_minio_user_prefix}/ex3-figure.pdf",
    )

