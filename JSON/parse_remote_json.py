import urllib.request
import json

#paresing remotely
#load will take jsn file return python object



with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/1") as url:
    data = json.load(url)
    print(data)