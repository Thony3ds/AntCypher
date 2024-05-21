import json

def lang_to_path(lang):
    if lang == "english":
        return "assets/langs/cmd/english.json"
    elif lang == "francais" or lang == "français" or lang == "french":
        return "assets/langs/cmd/french.json"

def modify_json(to_modify, value, file="assets/data/data_settings/settings.json"):
    print("Saving...")
    with open(file, 'r+') as json_file:
        data = json.load(json_file)
        if to_modify == "language":
            data[to_modify] = lang_to_path(value)
        else:
            data[to_modify] = value
        json_file.seek(0)
        json.dump(data, json_file, indent=4)
        json_file.truncate()
    print("Saving succefuly !")
def get_json(to_get, file="assets/data/data_settings/settings.json"):
    with open(file, 'r') as json_file:
        data = json.load(json_file)
        return data.get(to_get)