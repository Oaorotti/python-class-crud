import json
import os

def load_data_from_json(filename):
    if not os.path.isfile(filename) or os.path.getsize(filename) == 0:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump({}, file, indent=2)
        return {}
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_data_to_json(filename, dictionary_data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(dictionary_data, file, indent=2)