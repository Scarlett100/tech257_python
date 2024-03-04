import sys

import os

import subprocess

import json




# os
# os.mkdir("test-dir")

#  sys
if len(sys.argv) > 1:
    print("You gave me an argument!")   # command to run in terminal: python3 intro_to_scripting.py <insert anything>       basically the same as pressing the the run button but in terminal.

    #   if there is an argument run it is essentially what it is doing. that is what arg v does.  the 1 basically means " if there is something"
    # index 0 is the actual file!!!  The contents/argument of file are  index 1



# subprocess
process_1 = subprocess.run("ls")
print(process_1)
print(process_1.args)
print(process_1.returncode)
print(process_1.stdout)

subprocess.call(['python3', 'hello_world.py']) #runs the contents of the hello world file.


# json
x = {
    "name" : "Morgan",
    "age" : 5,
    "city" : "fdf"
}

y = json.dumps(x)  # this has changed our python dictionary to json! woooooow


print(type(x))
print(type(y))