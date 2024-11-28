# Programme pour trouver l'élément le plus fréquent dans une liste  
def element_plus_frequent(liste):  
    frequence = {}  
    
    # Compter la fréquence de chaque élément  
    for element in liste:  
        if element in frequence:  
            frequence[element] += 1  
        else:  
            frequence[element] = 1  

    # Trouver l'élément avec la fréquence maximale  
    max_element = liste[0]  
    max_count = frequence[max_element]  

    for element, count in frequence.items():  
        if count > max_count:  
            max_element = element  
            max_count = count  

    return max_element, max_count  

# Exemple de liste  
liste = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
element, count = element_plus_frequent(liste)  

# Affichage du résultat  
print(f"Le nombre le plus fréquent dans la liste est : {element} ({count} x)")
