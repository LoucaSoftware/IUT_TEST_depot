# Déclaration de la taille maximale des vecteurs  
nMax = 100 

v1 = []  
v2 = []  

# Demande à l'utilisateur d'entrer la taille effective des vecteurs  
while True:  
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))  
    if 1 <= n <= nMax:  
        break  
    else:  
        print(f"Veuillez entrer une valeur entre 1 et {nMax}.")  

# Saisie des composantes du premier vecteur v1  
print("Saisie du premier vecteur :")  
for i in range(n):  
    valeur = int(input(f"v1[{i}] = "))  
    v1.append(valeur)  

# Saisie des composantes du second vecteur v2  
print("Saisie du second vecteur :")  
for i in range(n):  
    valeur = int(input(f"v2[{i}] = "))  
    v2.append(valeur)  

# Calcul du produit scalaire v1 . v2  
produit_scalaire = round(float(sum(v1[i] * v2[i] for i in range(n))),1)  

# Affichage du résultat  
print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire}.")