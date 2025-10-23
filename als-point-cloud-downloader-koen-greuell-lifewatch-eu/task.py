import pathlib

import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--geospatial_shapefile', action='store', type=str, required=True, dest='geospatial_shapefile')


args = arg_parser.parse_args()
print(args)

id = args.id

geospatial_shapefile = args.geospatial_shapefile.replace('"','')



class GeolocationPoint:
    def __init__(self, latitude, longitude, altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def __repr__(self):
        return f"Point(latitude={self.latitude}, longitude={self.longitude}, altitude={self.altitude})"

"""
Get all geolocation points from the ALS database that are within the shapefile 
"""
def download_ALS_point_cloud(geospatial_shapefile):
    print(f"downloading data for {geospatial_shapefile}")

    dummy_data = [
        GeolocationPoint(latitude="52.3547426", longitude="4.9546608", altitude="-3.000"), 
        GeolocationPoint(latitude="55.6867243", longitude="12.5700724", altitude="13.000")
    ]
    return dummy_data

ALS_point_clouds = download_ALS_point_cloud(geospatial_shapefile)

ALS_point_cloud_file = "ALS_point_cloud_file.csv"
file_path = pathlib.Path(f'../tmp/data/{ALS_point_cloud_file}')
file_path.parent.mkdir(parents=True, exist_ok=True)
with open(file_path, 'w') as f:
    f.write(str(ALS_point_clouds))

file_ALS_point_cloud_file = open("/tmp/ALS_point_cloud_file_" + id + ".json", "w")
file_ALS_point_cloud_file.write(json.dumps(ALS_point_cloud_file))
file_ALS_point_cloud_file.close()
file_latitude = open("/tmp/latitude_" + id + ".json", "w")
file_latitude.write(json.dumps(latitude))
file_latitude.close()
