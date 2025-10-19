import json

def read_data_json(filename): # am i the only person who copy pastes this
    with open(filename, 'r') as f: # from project to project making only minor
        data = json.load(f) # Changes
    return data

def write_data_json(filename, entry):
    username = entry["username"]
    score = int(entry["score"])

    data = read_data_json(filename)

    if username not in data:
        data[username] = {"scores": []}

    if username != "Ilovepi3141" and score not in data[username]["scores"]:  
        data[username]["scores"].append(score)
        
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
