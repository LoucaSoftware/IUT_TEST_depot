somme = int(input("Entrez une somme d'argent en euros : "))  

# Décomposition de la somme  
billets_100 = somme // 100  
somme %= 100  

billets_50 = somme // 50  
somme %= 50  

billets_10 = somme // 10  
somme %= 10  

pieces_2 = somme // 2  
pieces_1 = somme % 2  

# Affichage des résultats  
resultat = f"{somme} euros, c'est donc {billets_100} billets de 100, {billets_50} billets de 50, " \
           f"{billets_10} billets de 10, {pieces_2} pièces de 2 et {pieces_1} pièce de 1."  
print(resultat)