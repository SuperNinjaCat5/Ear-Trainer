import json

def read_data_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def write_data_json(filename, new_entry):
    username = new_entry["username"]
    new_score = int(new_entry["score"])

    data = read_data_json(filename)

    if username not in data:
        data[username] = {"scores": []}

    data[username]["scores"].append(new_score)

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)