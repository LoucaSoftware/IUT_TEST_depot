L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]  

# Dictionnaire pour compter les occurrences  
count_dict = {}  

# Compter les occurrences de chaque élément dans la liste  
for number in L1:  
    if number in count_dict:  
        count_dict[number] += 1  
    else:  
        count_dict[number] = 1  

# Identifier l'élément le plus fréquent  
most_frequent = None  
max_count = 0  

for number in L1:  # Parcours dans l'ordre d'apparition  
    if count_dict[number] > max_count:  
        max_count = count_dict[number]  
        most_frequent = number  

# Affichage du résultat  
print(f"Le nombre le plus frequent dans la liste est le : {most_frequent} ({max_count} x)")


L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]  

# Initialiser les variables pour stocker le nombre le plus fréquent et son occurrence  
most_frequent = None  
max_count = 0  

# Parcourir chaque élément de la liste pour déterminer le plus fréquent  
for number in L1:  
    count = L1.count(number)  
    # Si le count est supérieur à max_count ou si c'est le premier nombre  
    if count > max_count:  
        max_count = count  
        most_frequent = number  

# Affichage du résultat  
print(f"Le nombre le plus frequent dans la liste est le : {most_frequent} ({max_count} x)")




""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
