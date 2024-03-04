import os

# Directory

directory = "test_dir"
parent_dir = "/Users/AAA"

# path
path = os.path.join(parent_dir, directory)
#basicallhy saying put the directory in the parent path (so in AAA)


#create the directory
os.mkdir(path)