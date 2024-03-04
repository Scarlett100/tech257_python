import yaml

path_to_yaml = 'example.yaml'  # doesn't have to be in variable
with open((path_to_yaml), 'r') as file:
    data = yaml.safe_load(file) #safe minutes


print(data)


