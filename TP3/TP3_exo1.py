# a) Calcul et affichage de la somme des N entiers naturels  
def somme_n_entiers():  
    N = int(input("Entrez un nombre entier N : "))  
    somme = sum(range(N + 1))  
    print(f"La somme des entiers de 0 à {N} est : {somme}")  

# b) Boucle d'attente qui se termine si l'utilisateur entre la valeur 100  
def boucle_attente():  
    while True:  
        valeur = int(input("Entrez une valeur (100 pour sortir) : "))  
        if valeur == 100:  
            break  

# c) Lecture de 10 valeurs réelles comprises entre 0 et 20  
def lecture_valeurs():  
    valeurs = []  
    while len(valeurs) < 10:  
        val = float(input("Entrez une valeur réelle entre 0 et 20 : "))  
        if 0 <= val <= 20:  
            valeurs.append(val)  
        else:  
            print("Valeur invalide. Veuillez réessayer.")  

    inf_10 = sum(1 for v in valeurs if v < 10)  
    entre_10_et_15 = sum(1 for v in valeurs if 10 <= v < 15)  
    superieur_15 = sum(1 for v in valeurs if v >= 15)  

    print(f"Nombre de valeurs inférieures strictement à 10 : {inf_10}")  
    print(f"Nombre de valeurs supérieures ou égales à 10 et inférieures strictement à 15 : {entre_10_et_15}")  
    print(f"Nombre de valeurs supérieures ou égales à 15 : {superieur_15}")  

# d) Calcul et affichage du plus grand nombre N tel que ∑(i=0 to N) i ≤ X  
def plus_grand_n():  
    X = int(input("Entrez un nombre supérieur à 1 : "))  
    N = 0  
    somme = 0  

    while somme + N <= X:  
        somme += N  
        N += 1  

    print(f"Le plus grand nombre N tel que la somme de 0 à N est ≤ {X} est : {N - 1}")  

# Appel des fonctions pour exécuter les différentes parties  
somme_n_entiers()  
boucle_attente()  
lecture_valeurs()  
plus_grand_n()