# TODO FILE:
# Partie en cours = 0b
Continuer la création de TODO.md

## 0 Créer l'architecture physique et mental:

a - Créer une architecture globale de la structure des dossiers et fichiers +\
créer les fichiers important (A remplir petit à petit)\
b - Etablir un TODO file avec une documentation normale sur le projet et ses étapes.\
Il est important de noter qu'il sera ajouté de la documentation de plus en plus détailler et que à cette étape, on a encore un point de vue globale !\
c - vérifier l'import de tous les assets nécessaire pour commencer. Les autres seront ajoutées petit à petit.

## Cette partie tous les cryptage seront fait seront un input d'un phrase sans carractères spéciaux (juste lettres)
## 1 Créer l'app le corp (non visuel):

a - créer le système de base du cryptage dans [AntCypher.py](assets/scripts/AntCypher.py)\
b - créer une interface dans le terminal avec [Run_App.py](interfaces/Cmd_Interface.py) pour crypter puis décrypter\
c - DEBUG l'app + apporter des modifs a TODO si nécessaire

## 2 Renfort du corp (non visuel):

a - créer un systeme de methodes avec une structure encoder spécialement dans un type de fichier spécial stocké dans [data/saved_methodes/](assets/scripts/AntCypher.py) \
b - créer la methode de décodage et modifier **AntCypher.py** pour qu'il puisse lire l'encodage de la fonction puis l'executer.\
c - modifier **AntCypher.py** pour qu'il puisse lire des methodes celon le path désiré.
d - modifier la **Cmd_Interface.py** pour avoir une command "help" qui ouvrira un fichier **assets/app_info/Help_HTU.md** avec une docu sur toutes les commandes\
e - créer des paramètres avec pour l'instant juste le chemin de la méthode à utiliser\
f - DEBUG l'app + apporter des modifs a TODO si nécessaire + Améliorer le cmd si possible

## 5 Créer le cryptage de tous type de carractères (d'un clavier azerty normale)

a - modifier le dictionnaire de l'alphabet
TODO - Des modification son à aporter une fois une construction globale établie
b - DEBUG l'app + apporter des modifs a TODO si nécessaire 

## 4 Créer l'Interface graphique:

a - Créer un GUI non relié a l'app (une base en gros) + DEBUG
b - Lier l'app GUI au prog AntCypher de façon simple (sans style)
c - DEBUG
d - Ajouter des éléments de style (ex: font, ...)

## 5 Continuer la création du TODO.md