import tkinter as tk
from tkinter import ttk, filedialog
from assets.SubPrograms.DATAFILES import datafiles

app = tk.Tk()

class Data():
    def __init__(self):
        self.langue = "English"
        self.save_data = "No Folder Select"
data = Data()

def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        data.save_data = folder_selected
        data.lab2.config(text=folder_selected)
        data.bu2.pack()

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

def page3():
    data.progress_bar.step(data.bar_step)
    # TODO CHANGE FILE PATH IN SETTINGS FILE
    data.lab1.config(text="Page 3")

def page2():
    data.progress_bar.step(data.bar_step)
    #datafiles.modify_json(to_modify="language", value=data.langue) TODO remove
    if data.langue == "français":
        lab1_text = "Choisissez un dossier de sauvegarde (Pas situer dans le dossier de l'application"
    else:
        lab1_text = "Select a directory for saves (Not in the app directory)"
    data.lab1.config(text=lab1_text)
    dropdown.destroy()
    data.bu1.destroy()
    data.select_file = tk.Button(app, text="Select Folder/Choisir un fichier", command=select_folder)
    data.select_file.pack()
    data.lab2 = tk.Label(app, text="")
    data.lab2.pack()
    data.bu2 = tk.Button(app, text="Validate / Valider", command=page3)

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