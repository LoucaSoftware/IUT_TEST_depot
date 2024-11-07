import random  

# Tire une valeur aléatoire entre 0 et 100  
x = random.randint(0, 100)  

# Initialisation du compteur de tentatives  
nombre_tentatives = 0  

# Boucle pour demander à l'utilisateur de deviner la valeur  
while True:  
    # Demande à l'utilisateur de faire une proposition  
    proposition = int(input("Devinez un nombre entre 0 et 100 : "))  
    nombre_tentatives += 1  # Incrémente le compteur à chaque proposition  

    # Vérifie si la proposition est correcte, trop grande ou trop petite  
    if proposition < 0 or proposition > 100:  
        print("Veuillez entrer un nombre entre 0 et 100.")  
    elif proposition < x:  
        print("C'est plus !")  
    elif proposition > x:  
        print("C'est moins !")  
    else:  
        print(f"Bravo ! Vous avez trouvé le nombre mystère {x} en {nombre_tentatives} tentatives.")  
        break  # Sort de la boucle si le nombre est trouvé