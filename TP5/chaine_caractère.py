# ChaînesDeCaractéristiques.py  

def taille_chaine(chaine):  
    """Retourne la taille de la chaîne de caractères."""  
    return len(chaine)  

def pourcentage_voyelles(chaine):  
    """Calcule le pourcentage de voyelles dans la chaîne de caractères."""  
    voyelles = "aeiouyAEIOUY"  
    nombre_voyelles = sum(1 for c in chaine if c in voyelles)  
    pourcentage = (nombre_voyelles / len(chaine)) * 100 if len(chaine) > 0 else 0  
    return pourcentage  

def rechercher_sous_chaine(chaine, sous_chaine):  
    """Cherche une sous-chaîne dans la chaîne principale et retourne sa première occurrence."""  
    index = chaine.find(sous_chaine)  
    return index if index != -1 else None  

def compter_occurrences(chaine, sous_chaine):  
    """Compte le nombre d'occurrences de la sous-chaîne dans la chaîne principale."""  
    return chaine.count(sous_chaine)  

# Prog principale  
if __name__ == "__main__":  
    # Entrée de l'utilisateur  
    chaine = input("Entrez une chaîne de caractères (max 100 caractères) : ")[:100]  

    # 1. Taille de la chaîne  
    taille = taille_chaine(chaine)  
    print(f"Taille de la chaîne : {taille}")  

    # 2. Pourcentage de voyelles  
    pourcentage_voyelles_resultat = pourcentage_voyelles(chaine)  
    print(f"Pourcentage de voyelles : {pourcentage_voyelles_resultat:.2f}%")  

    # 3. Recherche de la sous-chaîne "wagon"  
    sous_chaine = "wagon"  
    premiere_occurrence = rechercher_sous_chaine(chaine, sous_chaine)  
    if premiere_occurrence is not None:  
        print(f"La sous-chaîne '{sous_chaine}' est trouvée à l'index {premiere_occurrence}.")  
    else:  
        print(f"La sous-chaîne '{sous_chaine}' n'est pas trouvée.")  

    # 4. Nombre d'occurrences de la sous-chaîne "wagon"  
    nb_occurrences = compter_occurrences(chaine, sous_chaine)  
    print(f"Nombre d'occurrences de '{sous_chaine}' : {nb_occurrences}")