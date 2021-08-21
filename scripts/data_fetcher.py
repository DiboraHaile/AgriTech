import pdal
import json
from json import load, dumps
import sys
import geopandas as gpd
from shapely.geometry import Point

class FetchData:
    """ fetches data given public data path, region and polygon """
    def __init__(self,public_data_path,region,polygon_bound):
       # initialize variables
       self.public_data_path = public_data_path
       self.region = region
       self.public_access_path = self.public_data_path + self.region + "ept.json"
       self.polygon = polygon_bound
       # set and execute pipeline
       self.fetch_data()

    def fetch_data(self):
       self.set_pipeline_df()
       self.execute_pipeline()
       self.get_elevation()
 
    def set_pipeline_df(self):
       self.data_pipeline_json = json.load(open("../data/pipeline.json"))
       self.data_pipeline_json["pipeline"][0]['filename'] = self.public_access_path
       self.data_pipeline_json["pipeline"][1]['polygon'] = self.polygon
       self.pipeline = pdal.Pipeline(json.dumps(self.data_pipeline_json))

   
    def get_elevation(self):
        geodf = gpd.GeoDataFrame()
        elevations = []
        geometry = []
        for row in self.self.pipeline.arrays()[0]:
            value_list = row.tolist()[-3:]
            geometry.append(Point(value_list[0], value_list[1]))
            elevations.append(value_list[2])
        geodf['elevation'] = elevations
        geodf['geometry'] = geometry
        self.geodf = geodf.set_crs(epsg=4326)


    def execute_pipeline(self):
       self.count = self.pipeline.execute()

    def return_pipeline(self):
       return self.pipeline

    def return_elevation(self):
       return self.geodf
    

