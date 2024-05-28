import os, shutil, time, json # os.getcwd() = actual file
from git import Repo
def get_maj():
    print("Search for updates...")
    repo_url = 'https://github.com/Thony3ds/AntCypher.git'
    repo_dir = f"{os.getcwd()}/assets/SubPrograms/MERGE/update/"
    Repo.clone_from(repo_url, repo_dir)
    time.sleep(1)
    shutil.move("assets/SubPrograms/MERGE/update/updates.json", "assets/SubPrograms/MERGE/system_version/updates.json")

    with open("system_version/app_version.json") as file:
        with open("system_version/updates.json") as updates:
            sys_ver = json.load(file)
            update = json.load(updates)
            if sys_ver["version"] << update["version"]:
                question = input("New update is available do you want to do the update ? Y/n: ")
                if question == "Y":
                    print("Updating...")
                    update_app()
                else:
                    print("Update is important do it when you be ready")

def update_app():
    print("Update app")