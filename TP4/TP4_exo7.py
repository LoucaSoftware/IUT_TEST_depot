# tp4exo7.py  

# Étape 1 : Créer un tuplet nommé "binome"  
login1 = input("Entrez votre login : ")  
login2 = input("Entrez le login de votre voisin : ")  
binome = (login1, login2)  

# Affichage du message  
print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}.")  

# Étape 2 : Changer le binôme  
nouveau_login = input("Entrez le nouveau login pour le second membre du binôme : ")  
# Comme les tuplets sont immuables, nous devons créer un nouveau tuplet  
binome = (binome[0], nouveau_login)  
print(f"Nouveau binôme : L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}.")  

# Étape 3 : Essayer de supprimer le second élément  
try:  
    del binome[1]  
except TypeError as e:  
    print("Erreur : Les tuplets sont immuables et ne peuvent pas être modifiés.", str(e))  

# Étape 4 : Former un trinôme  
login3 = input("Entrez le login d'un troisième membre : ")  
trinome = (binome[0], binome[1], login3)  
print(f"Le trinôme est composé de : {trinome[0]}, {trinome[1]} et {trinome[2]}.")