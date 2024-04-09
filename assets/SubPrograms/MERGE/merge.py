import os, shutil, time
from git import Repo
def get_maj():
    print("Search for updates...")
    repo_url = 'https://github.com/Thony3ds/SubPrograms_Lib.git'
    repo_dir = f"{os.getcwd()}/assets/SubPrograms/MERGE/update/"
    Repo.clone_from(repo_url, repo_dir)
    time.sleep(1)
    shutil.move("assets/SubPrograms/MERGE/update/updates.json", "assets/SubPrograms/MERGE/system_version/updates.json")
    shutil. rmtree(f"{os.getcwd()}/assets/SubPrograms/MERGE/update/")
    #compare updates.json avec l'ancien json qui s'appellera: app_version.json pour chercher les maj
    # to_update = list()
    #for i in range(nombre d'elements): # i prend a chaque boucle une valeur d'un truc json
    #   for j in range(nombre d'elements update.json): #j prend ... comme i
    #       if i < j:
    #           to_update.append(titrej) = j
    #print(to_update)

def update_app():
    print("Update app")