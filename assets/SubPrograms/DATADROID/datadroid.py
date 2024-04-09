import json

def modify_settings(to_modify, value):
    print("Saving...")
    with open("assets/data/data_settings/settings.json", 'r+') as json_file:
        data = json.load(json_file)
        data[to_modify] = value
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()
    print("Saving succefuly !")
def get_settings(to_get):
    with open("assets/data/data_settings/settings.json", 'r') as json_file:
        data = json.load(json_file)
        return data.get(to_get)