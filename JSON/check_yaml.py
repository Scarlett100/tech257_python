
import os, yaml, sys

#how to validate on terminal
#python -c 'import yaml, sys; print(yaml.safe_load(sys.stdin))' < example.yaml <-- QUICKER WAY TO VALIDATE WITHOUT PYTHON NEEDED

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.safe_load(file)
        file.close()
        print("YAML is VALID!")
    else:
        print(sys.argv[1] + "not found")
else:
    print("Usage python check_.py <file>")


# MUST CHECK ON TERMINAL TO RUN : python3 check_yaml.py example.yaml