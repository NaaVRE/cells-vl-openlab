
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--ALS_point_cloud_file', action='store', type=str, required=True, dest='ALS_point_cloud_file')

arg_parser.add_argument('--serialized_plot_locations', action='store', type=str, required=True, dest='serialized_plot_locations')


args = arg_parser.parse_args()
print(args)

id = args.id

ALS_point_cloud_file = args.ALS_point_cloud_file.replace('"','')
serialized_plot_locations = json.loads(args.serialized_plot_locations)



class PlotLocation:
    def __init__(self, latitude_upper, latitude_lower, longitude_upper, longitude_lower):
        self.latitude_upper = latitude_upper
        self.latitude_lower = latitude_lower
        self.longitude_upper = longitude_upper
        self.longitude_lower = longitude_lower

    def to_json(self):
        return {
            "latitude_upper": self.latitude_upper,
            "latitude_lower": self.latitude_lower,
            "longitude_upper": self.longitude_upper,
            "longitude_lower": self.longitude_lower
        }

    def from_json(cls, data_dict):
        return cls(
            latitude_upper=data_dict['latitude_upper'],
            latitude_lower=data_dict['latitude_lower'],
            longitude_upper=data_dict['longitude_upper'],
            longitude_lower=data_dict['longitude_lower']
    )

class CellPointCloud:
    def __init__(self, cell_id, plot_location, geolocation_points):
        self.cell_id = cell_id # the unique indentifier number of the cell
        self.plot_location = plot_location
        self.geolocation_points = geolocation_points

def clip_point_cloud(plot_locations, point_cloud_data):
    dummy_cell_point_clouds = [
        CellPointCloud(
            cell_id=1,
            plot_location=serialized_plot_locations[0],
            geolocation_points = [point_cloud_data[0]]
            ),
         CellPointCloud(
            cell_id=1,
            plot_location=serialized_plot_locations[1],
            geolocation_points = [point_cloud_data[1]]
            )]                                  
    return dummy_cell_point_clouds

with open(ALS_point_cloud_file, 'r') as f:
     ALS_point_cloud = f.read()


clipped_ALS_point_clouds = clip_point_cloud(serialized_plot_locations, ALS_point_cloud)

file_clipped_ALS_point_clouds = open("/tmp/clipped_ALS_point_clouds_" + id + ".json", "w")
file_clipped_ALS_point_clouds.write(json.dumps(clipped_ALS_point_clouds))
file_clipped_ALS_point_clouds.close()
