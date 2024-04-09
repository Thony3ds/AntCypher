from assets.SubPrograms.ANTCYPHER import AntCypher
from assets.SubPrograms.MERGE import merge
from assets.SubPrograms.DATADROID import datadroid

def launch():
    print("CMD app launch...")
    print("AntCypher cmd: type help for more infos")
    command = ""
    while command != "exit_app_instant":
        command = input("AntCypher cmd: ")
        if command == "help":
            print("You can have help in AntCypher/assets/app_info/Help_How_To_Use.md\nType exit to quit the app")
        elif command == "exit":
            q = input("Do you want to exit Y/n ?")
            if q == "Y":
                command = "exit_app_instant"
                break
            else:
                print("Exit have been canceled")
        elif command == "exit_app_instant":
            print("Closing app...")
            print("! Warning ! Use this command can corrupt your data because some data can be not save.\nPlease use exit to be sure to save all data.")
        elif command == "crypt":
            message = input("Input the message: ")
            key = input("Input the key: ")
            print(AntCypher.crypt(message, key))
        elif command == "decrypt":
            message = input("Input the crypted message: ")
            key = input("Input the key: ")
            print(AntCypher.decrypt(message, key))
        elif command == "methode":
            var = input("Input your methode.json file path or DEFAULT: ")
            if var == "DEFAULT":
                var = "assets/data/saved_methodes/default_methode.json"
            else:
                var = f"assets/data/saved_methode/{var}"
            datadroid.modify_settings("used_methode", var)
        else:
            print(f"Error 404 :(\nNo found command: {command}")