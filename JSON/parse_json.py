import os, json
#paresing locally

path_to_json = "example.json"
json = json.loads(open(path_to_json).read())
#open the file, so we can get the data
#loads will take json string return python object


for key in json:
    value = json[key]
    print(f"The key is {key} and the value is {value}")

