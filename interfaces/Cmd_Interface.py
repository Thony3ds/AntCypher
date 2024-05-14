from assets.SubPrograms.ANTCYPHER import AntCrypt, AntDecrypt
from assets.SubPrograms.MERGE import merge
from assets.SubPrograms.DATADROID import datadroid

def launch():
    print("CMD app launch...")
    print("AntCypher cmd: type help for more infos")
    command = ""
    while command != "exit_app_instant":
        command = input("AntCypher cmd: ")
        if command == "help":
            commands = open("assets/app_info/Help_In_Cmd.txt", "r")
            print(commands.read())
        elif command == "exit" or command == "quit":
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
            file_name = input("Input the file path: ")
            file_exit = input("Input the output file name: ")
            method = input("Input the method name: ")
            key = input("Input the key (If needed): ")
            print(AntCrypt.encrypt_file(filename=file_name, file_exit=file_exit, method=method, key=key))
        elif command == "decrypt":
            file_name = input("Input the file path: ")
            file_exit = input("Input the output file name: ")
            method = input("Input the method name: ")
            key = input("Input the key (If needed): ")
            print(AntDecrypt.decrypt_file(filename=file_name, file_exit=file_exit, method=method, key=key))
        else:
            print(f"Error 404 :(\nNo found command: {command}")