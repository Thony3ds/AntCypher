import os, shutil, json

def get_json(to_get, file="settings.json"):
    with open(file, 'r') as json_file:
        data = json.load(json_file)
        return data.get(to_get)

def BUS():
    print("----------Basic Updater System----------")
    print("Start updating...")

    print("\n0% --- Removing old app...")
    #var = get_json(to_get=)
    #os.rmdir()

if __name__ == "__main__":
    BUS()