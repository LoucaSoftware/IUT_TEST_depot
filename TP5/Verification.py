# Verification.py  

import os  
from datetime import datetime  

def obtenir_info_fichier(nom_fichier):  
    """Retourne la taille et la date de dernière modification d'un fichier."""  
    if os.path.isfile(nom_fichier):  
        taille = os.path.getsize(nom_fichier)  
        derniere_modification = os.path.getmtime(nom_fichier)  
        date_modification = datetime.fromtimestamp(derniere_modification)  
        return taille, date_modification  
    else:  
        return None, None  

def main():  
    # Demande à l'utilisateur de saisir les noms des fichiers  
    fichier1 = input("Entrez le nom du premier fichier : ")  
    fichier2 = input("Entrez le nom du second fichier : ")  

    # Obtenir les informations pour chaque fichier  
    taille1, date1 = obtenir_info_fichier(fichier1)  
    taille2, date2 = obtenir_info_fichier(fichier2)  

    # Afficher les tailles et les dates de modification  
    if taille1 is not None:  
        print(f"Fichier 1 : {fichier1} - Taille : {taille1} octets, Dernière modification : {date1}")  
    else:  
        print(f"Fichier 1 : {fichier1} n'existe pas.")  

    if taille2 is not None:  
        print(f"Fichier 2 : {fichier2} - Taille : {taille2} octets, Dernière modification : {date2}")  
    else:  
        print(f"Fichier 2 : {fichier2} n'existe pas.")  

    # Déterminer lequel des fichiers a été modifié le plus récemment  
    if date1 and date2:  
        if date1 > date2:  
            print(f"Le fichier le plus récent est : {fichier1}")  
        elif date2 > date1:  
            print(f"Le fichier le plus récent est : {fichier2}")  
        else:  
            print("Les fichiers ont été modifiés à la même date.")  
    elif date1:  
        print(f"Le fichier le plus récent est : {fichier1}")  
    elif date2:  
        print(f"Le fichier le plus récent est : {fichier2}")  
    else:  
        print("Aucun des fichiers n'existe.")  

if __name__ == "__main__":  
    main()