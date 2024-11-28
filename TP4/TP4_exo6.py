# Déclaration de la liste initiale  
tab = [5, 2, 4, 8, 1, 3]  

# Affichage de l'état initial de la liste  
print(f"État initial : {tab}")  

# Tri de la liste par la méthode du tri par sélection  
n = len(tab)  

for i in range(n):  
    # On suppose que le i-ème élément est le minimum  
    min_index = i  
    for j in range(i + 1, n):  
        if tab[j] < tab[min_index]:  
            min_index = j  
            
    # Échanger l'élément trouvé (tab[min_index]) avec tab[i]  
    tab[i], tab[min_index] = tab[min_index], tab[i]  
    
    # Afficher l'évolution du tableau après chaque phase  
    print(f"Phase {i} : {tab}")  

# Affichage final  
print(f"Liste triée : {tab}")  

# Exécution du code standard Python pour le tri  
print("\nUtilisation de sorted() :")  
print(sorted(tab))  # Affiche le tableau trié sans le modifier  

# Affichage de la liste après l'utilisation de sorted()  
print(f"Liste après sorted() : {tab}")  

# Utilisation de sort() pour trier la liste sur place  
tab.sort()  
print(f"Liste après sort() : {tab}")