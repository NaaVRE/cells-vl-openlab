
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--clipped_ALS_point_clouds', action='store', type=str, required=True, dest='clipped_ALS_point_clouds')


args = arg_parser.parse_args()
print(args)

id = args.id

clipped_ALS_point_clouds = json.loads(args.clipped_ALS_point_clouds)



def filter_non_ground_points(point_cloud):
    return "non ground points"

non_ground_ALS_point_clouds = []
for clipped_ALS_point_cloud in clipped_ALS_point_clouds:
    non_ground_ALS_point_clouds.append(filter_non_ground_points(clipped_ALS_point_cloud))

