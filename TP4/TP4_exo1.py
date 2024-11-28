Nombre = float(input("Vous cherchez la table de multiplication de quel nombre ?"))
Resultat = 1
for i in range (0, 11, 1):
    Resultat = Nombre * i
    print(f"{Nombre} * {i} = {round(Resultat, 1)}")

#Code de exos 
# Fonction pour générer la table de multiplication  
def table_multiplication(nombre):  
    resultats = []  
    for i in range(10):  
        resultat = round(nombre * i, 1)  # Multiplication arrondie à 1 décimale  
        resultats.append(f"{nombre} * {i} = {resultat}")  # Formatage du résultat  
    return resultats  

# Demande à l'utilisateur
nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))  

# Affichage
resultats = table_multiplication(nombre)  
for resultat in resultats:  
    print(resultat)