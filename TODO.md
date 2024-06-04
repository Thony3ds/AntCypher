# TODO FILE:
# Partie en cours = **_5a_** 
# Pour toutes étapes regarder ALPHA !
## ALPHA: Maj SYS:
Mettre à jour le système de fichiers pour créer des sous programmes indépenant qui aide (et aide a la structuration du projet) :\
a - MERGE (Systeme de mise à jour qui pourra aller dans un répértoire github pour chercher 1 fichier de maj lib request)\
et qui pourra maj avec gitpython voir [TODO_MERGE](assets/SubPrograms/MERGE/TODO.md)\
b - SYSFILE (Objectifs : toutes les demandes de fichiers / read JSON passe par lui)\
c - ANTCYPHER (Concerne tout ce qui est cryptage)
d - LANG (SYSTEME Multilangue)
e - DATADROID (Gere l'encodage de la data)

## 0 Créer l'architecture physique et mental :

a - Créer une architecture globale de la structure des dossiers et fichiers +\
créer les fichiers important (A remplir petit à petit)\
b - Etablir un TODO file avec une documentation normale sur le projet et ses étapes.\
Il est important de noter qu'il sera ajouté de la documentation de plus en plus détailler et que à cette étape, on a encore un point de vue globale !\
c - vérifier l'import de tous les assets nécessaire pour commencer. Les autres seront ajoutées petit à petit.

## Cette partie tous les cryptages seront fait seront un input d'une phrase sans carractères spéciaux (juste lettres)
## L'interface sera en anglais pour cette partie
## 1 Créer l'app le corp (non visuel) :

a - créer le système de base du cryptage dans [AntCypher.py](assets/SubPrograms/ANTCYPHER/AntCrypt.py)\
b - créer une interface dans le terminal avec [Run_App.py](interfaces/Cmd_Interface.py) pour crypter puis décrypter\
c - DEBUG l'app + apporter des modifs à TODO si nécessaire

## 2 Renfort du corp (non visuel) :

a - créer un systeme de methodes avec une structure encoder spécialement dans un type de fichier spécial stocké dans [data/saved_methodes/](assets/SubPrograms/ANTCYPHER/AntCrypt.py) \
b - créer la methode de décodage et modifier **AntCypher.py** pour qu'il puisse lire l'encodage de la fonction puis l'executer.\
c - modifier **AntCypher.py** pour qu'il puisse lire des methodes celon le path désiré.\

INFO - 2abc ont été modifié le plan n'est plus celui utilisé\

d - modifier la **Cmd_Interface.py** pour avoir une command "help" qui ouvrira un fichier **assets/app_info/Help_HTU.md** avec une docu sur toutes les commandes\
e - créer des paramètres ... N'est plus dans la liste\
f - DEBUG l'app + apporter des modifs a TODO si nécessaire + Améliorer le cmd si possible

## 3 Créer le cryptage de tous type de carractères (d'un clavier azerty normale)

a - modifier le dictionnaire de l'alphabet
TODO - Des modifications sont à aporter une fois une construction globale établie\
b - DEBUG l'app + apporter des modifs a TODO si nécessaire 

## 4 Inclure une interface multilangues

a - Créer des fichiers Json contenant une version française de l'appli (la docu reste en anglais pour l'instant)\
b - Adapter les versions de langue à pouvoir être misent sur l'application graphique et sur le terminal (1 fichier par langues)\
c - Relir pour les fautes d'orthographe dans toutes les langues\
d - DEBUG l'app + apporter des modifs a TODO si nécessaire 

## 5 Créer le système de mise a jour

a - créer une fonction qui met les fichiers modifier (settings, ...) dans un dossier safe
b - mettre a jour l'app SI le num de version est suppérieur SINON RIEN
c - utiliser git pour mettre a jour l'app
d - tester la fonction de maj
e - DEBUG l'app + apporter des modifs a TODO si nécessaire

## _6 Modifier le TODO pour aporter des modifs/améliorations a l'app_
## 7 Ecrire la documentation et autres fichiers
a - écrire le README.md
b - écrire le Release_Notes.md
c - écrire le Help_HTU.md
d - écrire la LICENSE.md
e - écrire d'autres documents si nécessaire
f - vérifier l'integralité de l'app

## NUM Créer l'Interface graphique:

a - Créer un GUI non relié a l'app (une base en gros) + DEBUG
b - Lier l'app GUI au prog AntCypher de façon simple (sans style)
c - DEBUG
d - Ajouter des éléments de style (ex: font, ...)
e - DEBUG l'app + apporter des modifs a TODO si nécessaire 

## NUM Costumisation de l'app:

a - ajout d'un systeme pour changer la font prise (necessite une font a mettre dans assets/fonts/)


Changer merge.py pour mettre le get_maj en raw sur system_version.json