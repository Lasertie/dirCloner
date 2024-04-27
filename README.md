[Version francaise](#dircloner-fr) | [English version](#dircloner-en)
# dirCloner fr
Un petit script python pour cloner un répertoire et son contenu de maniere recursive.

## Fonctionnement
Le dossier source et son contenu seront copie dans le dossier destination de maniere recursive en __**supprimant**__ les fichiers existants dans le dossier destination.

## Utilisation (version executable)
1. Telecharger le projet en selectionnant la "release" la plus recente dans la section "Releases"
2. Extraire le contenu du fichier ZIP


## Utilisation (version script python)
1. Telecharger le projet en cliquant sur le bouton vert "Code" puis "Download ZIP"
2. Extraire le contenu du fichier ZIP
3. Installer les dependances avec la commande `pip install -r requirements.txt`
4. Lancez le script avec la commande `python main.py`
    * Lors de la premiere execution, un fichier "config.ini" sera cree.
5. Modifier le fichier "config.ini" pour y ajouter les chemins du dossiers a cloner et du dossier de destination. ("source" et "destination")
6. Relancer le script

## Configuration
Le fichier "config.ini" contient les informations suivantes:
* source: Chemin du dossier a cloner
* destination: Chemin du dossier de destination

## Dependances
* shutil
* configparser

## Auteur
### [Lasertie](https://github.com/Lasertie)

## License
Ce projet est sous license [MIT](https://choosealicense.com/licenses/mit/)


# dirCloner en
A small python script to clone a directory and its content recursively.

## How it works
The source directory and its content will be copied to the destination directory recursively by __**deleting**__ existing files in the destination directory.

## Usage (executable version)
1. Download the project by clicking on the green button "Code" then "Download ZIP"
2. Extract the content of the ZIP file
3. Go to the "dist" folder then run the "main.exe" file
    * On the first run, a "config.ini" file will be created.
4. Modify the "config.ini" file to add the paths of the folders to be cloned and the destination folder. ("source" and "destination")
5. Restart the "main.exe" file

## Usage (python script version)
1. Download the project by clicking on the green button "Code" then "Download ZIP"
2. Extract the content of the ZIP file
3. Install the dependencies with the command `pip install -r requirements.txt`
4. Run the script with the command `python main.py`
    * On the first run, a "config.ini" file will be created.
5. Modify the "config.ini" file to add the paths of the folders to be cloned and the destination folder. ("source" and "destination")
6. Restart the script

## Configuration
The "config.ini" file contains the following information:
* source: Path of the folder to be cloned
* destination: Path of the destination folder

## Dependencies
* shutil
* configparser

## Author
### [Lasertie](github.com/Lasertie)

## License
This project is under the [MIT](https://choosealicense.com/licenses/mit/) license
