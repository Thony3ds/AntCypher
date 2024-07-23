import os, shutil, time, json, requests # os.getcwd() = actual file
from git import Repo
from assets.SubPrograms.DATAFILES import datafiles
def get_maj():
    print("Search for updates...")
    # Remplacez 'URL_DU_FICHIER_RAW' par le lien raw du fichier que vous souhaitez cloner
    url = 'https://raw.githubusercontent.com/Thony3ds/AntCypher/master/assets/SubPrograms/MERGE/system_version/app_version.json'
    # Effectuez une requête GET pour obtenir le contenu du fichier
    reponse = requests.get(url)

    # Si requete reussi
    if reponse.status_code == 200:
        # Écrire le contenu dans un fichier local
        with open('assets/SubPrograms/MERGE/system_version/update.json', 'wb') as file:
            file.write(reponse.content)

    time.sleep(1)
    with open("assets/SubPrograms/MERGE/system_version/app_version.json") as file:
        with open("assets/SubPrograms/MERGE/system_version/update.json") as updates:
            sys_ver = json.load(file)
            update = json.load(updates)
            if sys_ver["version"] < update["version"]:
                question = input("New update is available do you want to do the update ? Y/n: ")
                if question == "Y" or question == "O":
                    print("Updating...")
                    update_app()
                else:
                    print("Updates are important do it when you be ready")

def copy_file(source_path, destination_path):
    with open(source_path, 'rb') as source_file:
        with open(destination_path, 'wb') as destination_file:
            destination_file.write(source_file.read())

def update_app():
    print("Update app...")
    repo_url = 'https://github.com/Thony3ds/AntCypher.git'
    repo_dir = f"{os.getcwd()}/assets/SubPrograms/MERGE/update/"
    Repo.clone_from(repo_url, repo_dir)
    time.sleep(1)
    temp_dir = datafiles.get_json(to_get="save_folder")
    copy_file(source_path=f"{os.getcwd()}/assets/data/data_settings/settings.json", destination_path=f"{temp_dir}settings.json")
    copy_file(source_path=f"{os.getcwd()}/assets/SubPrograms/MERGE/BUS_updater.py", destination_path=f"{temp_dir}BUS_updater.py")
    shutil.copytree(f"{os.getcwd()}/assets/SubPrograms/MERGE/update/", f"{temp_dir}update/")