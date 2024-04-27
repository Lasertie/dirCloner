import os
import shutil
import schedule
import time
import json

def synchroniser_dossiers(dossier_source, dossier_destination):
    # Vérifier si les dossiers existent
    if not os.path.exists(dossier_source):
        print("Le dossiers source n'existe pas.")
        return
    if not os.path.exists(dossier_destination):
        print("Le dossiers destination n'existe pas.")
        return
    
    # Parcourir les fichiers du dossier source
    for nom_fichier in os.listdir(dossier_source):
        chemin_source = os.path.join(dossier_source, nom_fichier)
        chemin_destination = os.path.join(dossier_destination, nom_fichier)

        # Vérifier si le fichier existe déjà dans le dossier destination
        if os.path.exists(chemin_destination):
            # Vérifier si le fichier est plus récent dans le dossier source
            if os.path.getmtime(chemin_source) > os.path.getmtime(chemin_destination):
                # Remplacer le fichier dans le dossier destination
                shutil.copy2(chemin_source, chemin_destination)
                print(f"Le fichier {nom_fichier} a été mis à jour.")
        else:
            # Copier le fichier dans le dossier destination
            shutil.copy2(chemin_source, chemin_destination)
            print(f"Le fichier {nom_fichier} a été ajouté.")
    # Supprimer les fichiers du dossier destination qui ne sont pas dans le dossier source
    for nom_fichier in os.listdir(dossier_destination):
        chemin_source = os.path.join(dossier_source, nom_fichier)
        chemin_destination = os.path.join(dossier_destination, nom_fichier)

        if not os.path.exists(chemin_source):
            os.remove(chemin_destination)
            print(f"Le fichier {nom_fichier} a été supprimé.")
    print("La synchronisation des dossiers est terminée.")

# Dossiers à synchroniser
def check_config_file():
    config_file = 'config.json'
    
    if not os.path.exists(config_file):
        # Create config.json file
        with open(config_file, 'w') as file:
            json.dump({"1": {"source": "/path/to/source", "destination": "/path/to/destination"}}, file)
        print("config.json file created.")
    
    # Read config.json file
    with open(config_file, 'r') as file:
        config = json.load(file)
    
    # Assign values to variables
    dossiers_source_destination = [(item['source'], item['destination']) for item in config.values()]
    
    return dossiers_source_destination

# Call the function to get the values
dossiers_source_destination = check_config_file()

for dossier_source, dossier_destination in dossiers_source_destination:
    synchroniser_dossiers(dossier_source, dossier_destination)
    # Planifier l'exécution de la fonction toutes les heures
    schedule.every(10).seconds.do(synchroniser_dossiers, dossier_source, dossier_destination)

# Boucle infinie pour exécuter les tâches planifiées
while True:
    schedule.run_pending()
    time.sleep(1)