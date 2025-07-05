import json

def read_data_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def write_data_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4) 