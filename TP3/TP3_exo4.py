# Fonction pour calculer la factorielle avec une boucle for  
def factorielle_for(n):  
    resultat = 1  
    for i in range(1, n + 1):  
        resultat *= i  
        print(f"Après multiplication par {i}, la factorielle est : {resultat}")  
    return resultat  

# Fonction pour calculer la factorielle avec une boucle while  
def factorielle_while(n):  
    resultat = 1  
    i = 1  
    while i <= n:  
        resultat *= i  
        print(f"Après multiplication par {i}, la factorielle est : {resultat}")  
        i += 1  
    return resultat  

# Demander à l'utilisateur de saisir un entier positif  
n = int(input("Veuillez saisir un entier positif pour calculer sa factorielle : "))  

# Demander à l'utilisateur de choisir le type de boucle  
choix = input("Choisissez le type de boucle (for/while) : ").strip().lower()  

if choix == "for":  
    print(f"La factorielle de {n} est : {factorielle_for(n)}")  
elif choix == "while":  
    print(f"La factorielle de {n} est : {factorielle_while(n)}")  
else:  
    print("Choix non valide. Veuillez choisir 'for' ou 'while'.")