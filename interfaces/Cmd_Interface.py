from assets.SubPrograms.ANTCYPHER import AntCypher
from assets.SubPrograms.MERGE import merge

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
        elif command == "merge":
            print("Test MERGE.get_maj() SubProgram...")
            merge.get_maj()
        else:
            print(f"Error 404 :(\nNo found command: {command}")