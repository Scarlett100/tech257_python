
import json
import os
import sys
import yaml

if len(sys.argv) > 1:   #

    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)   # how to convert into yaml


        source_file.close()   # closes file so that it works

        #  save the conversion in a new file output.json
        json_data = json.dumps(source_content) # dYAML 2 JSON is dumps


        with open(sys.argv[2], "w") as jsonl1st: # what we want to give a reference  name , just a way for computer to realise it is called yamlist
            jsonl1st.write(json_data) # giving permission
            print(json_data) # where you are storing
    else:
        print(f"error {sys.argv[1]} not found")
        exit(1)
else:
    print(f"Usage: python yaml2json.py <source_json_file.json> <target_yaml_file.yaml")


# python3 yaml2json.py example.yaml example1.json <-- copies yaml file to json
