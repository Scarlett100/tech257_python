import json
import os
import sys
import yaml


#

if len(sys.argv) > 1:   #

    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)   # how to convert into json


        source_file.close()   # closes file so that it works

        #  save the conversion in a new file output.yaml
        yaml_data = yaml.dump(source_content) # dumping content into a new bucket, don't have to specify until in terminal


        with open(sys.argv[2], "w") as yaml1st: # what we want to give a reference  name , just a way for computer to realise it is called yamlist
            yaml1st.write(yaml_data) # giving permission
            print(yaml_data) # where you are storing
    else:
        print(f"error {sys.argv[1]} not found")
        exit(1)
else:
    print(f"Usage: python json2yaml.py <source_json_file.json> <target_yaml_file.yaml")

    #  process the conversion - use yaml libray









