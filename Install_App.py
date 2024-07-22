import tkinter as tk
from tkinter import ttk, filedialog
import platform, os
from assets.SubPrograms.DATAFILES import datafiles

app = tk.Tk()

class Data():
    def __init__(self):
        self.langue = "English"
        self.save_data = "No Folder Select"
        # Variables pour les boutons à cocher
        self.default_var = tk.BooleanVar()
        self.custom_var = tk.BooleanVar()
        self.os_name = platform.system()
        self.user_name = os.getlogin()
data = Data()

def save_folder_default():
    if data.os_name == "Windows":
        return f"C:/Users/{data.user_name}/AppData/Local/AntCypher/"
    elif data.os_name == "Linux":
        return f"home/{data.user_name}/.local/share/AntCypher/"
    elif data.os_name == "Darwin": # (Mac OS)
        return f"/Users/{data.user_name}/Library/Application Support/AntCypher/"
    else:
        raise ValueError("Unsupported operating system")

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        data.save_data = folder_selected
        data.lab2.config(text=folder_selected)

    else:
        data.save_data = "No folder select"
        data.lab2.config(text="Error: No folder select")

def create_optbar(the_app): # Crée une bar avec des langues à choisir
    # Options de la liste déroulante
    global dropdown
    options = ["english", "français"]

    # Fonction appelée lorsque l'option est sélectionnée
    def on_select(event):
        data.langue = str(dropdown.get()) # recupere la langue

    # Création de la liste déroulante
    dropdown = ttk.Combobox(the_app, values=options, width=25)
    dropdown.pack()
    dropdown.insert(tk.END, "Select a language")

    # Définition de la fonction à appeler lorsque l'option est sélectionnée
    dropdown.bind("<<ComboboxSelected>>", on_select)

def on_default_checked():
    if data.default_var.get():
        data.custom_var.set(False)
        data.select_file.config(state="disabled")
        data.save_data = save_folder_default()
        data.lab2.config(text=data.save_data)
    else:
        data.select_file.config(state='normal')

def on_custom_checked():
    if data.custom_var.get():
        data.default_var.set(False)
        data.select_file.config(state='normal')

def page3():
    data.progress_bar.step(data.bar_step)
    #datafiles.modify_json(to_modify="save_folder", value=data.save_data)
    data.lab1.config(text="Page 3")
    data.default_check.destroy()
    data.custom_check.destroy()
    data.select_file.destroy()
    data.lab_file.destroy()
    data.lab2.destroy()
    data.bu2.destroy()
    if data.langue == "français":
        lab_txt = "Tout est prêt !"
    else:
        lab_txt = "Everything is ok !"
    lab = tk.Label(app, text=lab_txt)
    lab.pack()
    bu = tk.Button(app, text="Ok", command=app.quit)
    bu.pack()

def page2():
    data.progress_bar.step(data.bar_step)
    #datafiles.modify_json(to_modify="language", value=data.langue)
    if data.langue == "français":
        lab1_text = "Choisissez un dossier de sauvegarde (Pas situer dans le dossier de l'application)"
        bu2_txt = "Valider"
        select_txt = "Choisir un fichier"
    else:
        lab1_text = "Select a directory for saves (Not in the app directory)"
        bu2_txt = "Validate"
        select_txt = "Select a folder"
    data.lab1.config(text=lab1_text)
    dropdown.destroy()
    data.bu1.destroy()
    # Bouton à cocher "Default"
    data.default_check = ttk.Checkbutton(app, text="Default", variable=data.default_var, command=on_default_checked)
    data.default_check.pack()

    # Bouton à cocher "Custom"
    data.custom_check = ttk.Checkbutton(app, text="Custom", variable=data.custom_var, command=on_custom_checked)
    data.custom_check.pack()

    data.select_file = tk.Button(app, text=select_txt, command=select_folder)
    data.select_file.pack()
    data.lab_file = tk.Label(app, text=f"Folder path / Chemin du dossier:")
    data.lab_file.pack()
    data.default_var.set(True)
    data.select_file.config(state="disabled")
    data.lab2 = tk.Label(app, text=save_folder_default())
    data.lab2.pack()
    data.bu2 = tk.Button(app, text=bu2_txt, command=page3)
    data.bu2.pack()

def appli():
    app.title("Install AntCypher")
    app.geometry("800x800")
    app.option_add("*Font", "arial 24")

    data.lab_bar = tk.Label(app, text="Installation Progress")
    data.lab_bar.pack()
    data.progress_bar = ttk.Progressbar(app, orient="horizontal")
    data.progress_bar.pack()
    data.bar_step = 33
    data.lab1 = tk.Label(app, text="Welcome if you click on Validate you will accept Users Conditions")
    data.lab1.pack()
    create_optbar(app)
    data.bu1 = tk.Button(app, text="Validate", command=page2)
    data.bu1.pack()

    app.mainloop()

if __name__ == "__main__":
    appli()