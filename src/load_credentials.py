import json


def LoadCredentials(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] create your own 'credentials.json' file from example.credentials.json in {path}")
        exit()
    return data
