import json
import pdal 
import os
import sys
sys.path.append(os.path.abspath(os.path.join('../')))

class FetchData():
    def __init__(self,public_data_path,region,bounds,pipeline_def):
        self.pipeline_df = pipeline_def
        self.public_data_path = public_data_path
        self.region = region
        self.public_access_path = self.public_data_path + self.region + "ept.json"
        self.bounds = bounds
        self.pipeline_def = pipeline_def
        self.output_file = "data/data.geojson"
        self.set_pipeline_df()
        self.execute_pipeline()

    def set_pipeline_df(self):
        # self.pipeline_def[-1]["filename"] = self.output_file
        self.pipeline_def[0]['filename'] = self.public_access_path
        print(self.pipeline_def)
        self.pipeline_def[0]['bounds'] = self.bounds
        pipeline_json =  json.dumps(self.pipeline_def)
        self.pipeline = pdal.Pipeline(pipeline_json)

    def execute_pipeline(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
            
        self.pipeline.execute()
        data = open(self.output_file, 'r').read()
        data = data.replace("[,{", "[{").replace("}{", "},{")
        open(self.output_file, 'w').write(data)

        