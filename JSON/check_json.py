import os, json, sys


# python3 check_json.py
# python check_json.py example.json

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is VALID!")
    else:
        print(sys.argv[1] + "not found")
else:
    print("Usage python check_json.py <file>")


 # MUST CHECK ON TERMINAL TO RUN : python3 check_json.py example.json