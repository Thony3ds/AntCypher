from assets.SubPrograms.ANTCYPHER import AntCrypt, AntDecrypt
from assets.SubPrograms.MERGE import merge
from assets.SubPrograms.DATAFILES import datafiles

def launch():
    print(datafiles.get_json("cmd_launch", datafiles.get_json("language")))
    print(datafiles.get_json("cmd_launch2", datafiles.get_json("language")))
    command = ""
    while command != "exit_app_instant":
        command = input("AntCypher cmd: ")
        if command == "help":
            commands = open("assets/app_info/Help_In_Cmd.txt", "r")
            print(commands.read())
        elif command == "exit" or command == "quit":
            q = input(datafiles.get_json("exit_question", datafiles.get_json("language")))
            if q == "Y":
                command = "exit_app_instant"
                break
            else:
                print(datafiles.get_json("exit_cancel", datafiles.get_json("language")))
        elif command == "exit_app_instant":
            print(datafiles.get_json("closing_app", datafiles.get_json("language")))
            print(datafiles.get_json("closing_app2", datafiles.get_json("language")))
        elif command == "crypt":
            file_name = input(datafiles.get_json("crypt1", datafiles.get_json("language")))
            file_exit = input(datafiles.get_json("crypt2", datafiles.get_json("language")))
            method = input(datafiles.get_json("crypt3", datafiles.get_json("language")))
            key = input(datafiles.get_json("crypt4", datafiles.get_json("language")))
            print(AntCrypt.encrypt_file(filename=file_name, file_exit=file_exit, method=method, key=key))
        elif command == "decrypt":
            file_name = input(datafiles.get_json("decrypt1", datafiles.get_json("language")))
            file_exit = input(datafiles.get_json("decrypt2", datafiles.get_json("language")))
            method = input(datafiles.get_json("decrypt3", datafiles.get_json("language")))
            key = input(datafiles.get_json("decrypt4", datafiles.get_json("language")))
            print(AntDecrypt.decrypt_file(filename=file_name, file_exit=file_exit, method=method, key=key))
        elif command == "lang":
            question = input(datafiles.get_json("change_lang", datafiles.get_json("language")))
            if question == "francais" or question == "français" or question == "frensh" or question == "english":
                datafiles.modify_json(to_modify="language", value=question)
            else:
                print("Error 404")
        elif command == "update":
            #merge.get_maj() TODO remove
            merge.update_app()
        else:
            print(datafiles.get_json("error404", datafiles.get_json("language")), command)