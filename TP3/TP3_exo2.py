#BOUCLE FOR

import time  

# Demander à l'utilisateur de saisir un nombre entier positif  
n = int(input("Veuillez saisir un nombre entier positif : "))  

# Affichage avec une boucle for  
for i in range(n, -1, -1):  
    print(i)  
    time.sleep(1)  # Pause de 1 seconde entre chaque affichage


#Boucle While
import time  

# Demander à l'utilisateur de saisir un nombre entier positif  
n = int(input("Veuillez saisir un nombre entier positif : "))  

# Affichage avec une boucle while  
i = n  
while i >= 0:  
    print(i)  
    time.sleep(1)  # Pause de 1 seconde entre chaque affichage  
    i -= 1  # Décrementer i pour passer au nombre suivant



