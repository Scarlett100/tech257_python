import os


# Directory

directory = "test_dir"


#  path to parent directory
parent_dir = "/Users/AAA"


# path
path = os.path.join(parent_dir, directory)

# filename and path
filename = "testfile.txt"
filepath = os.path.join(path, filename)
# what you want to call the file and where you want to put it.


# make the file

with open(os.path.join(path, filename), "w") as file1:  #could have used filepath variable instead in second brackets, jujst means you dont need (path, filename) instead just : (os.path.join(filepath))
    toFile ="Content of the file are there"
    file1.write(toFile)
print(f"File {filename} created in {directory}")