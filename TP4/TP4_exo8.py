# tp4exo8.py  

# Étape 1 : Création du dictionnaire avec les informations de l'étudiant  
name = input("Entrez votre nom : ")  
firstname = input("Entrez votre prénom : ")  
promo = input("Entrez votre promotion : ")  
group = input("Entrez votre groupe : ")  

etudiant = {  
    "name": name,  
    "firstname": firstname,  
    "promo": promo,  
    "group": group  
}  

# Étape 2 : Affichage des données de l'étudiant  
print(f"Votre nom est '{etudiant['name']}', prénom est '{etudiant['firstname']}', "  
      f"vous faites partie de la promo '{etudiant['promo']}' et votre groupe est '{etudiant['group']}'.")  

# Étape 3 : Affichage du contenu du dictionnaire  
print("\nLes clés du dictionnaire sont :")  
for key in etudiant.keys():  
    print(f"- {key}")  

print("\nLes valeurs du dictionnaire sont :")  
for value in etudiant.values():  
    print(f"- {value}")  

print("\nLes tuplets du dictionnaire sont :")  
for item in etudiant.items():  
    print(f"- {item}")  

# Étape 4 : Ajout d'un autre étudiant  
name2 = input("\nEntrez le nom du deuxième étudiant : ")  
firstname2 = input("Entrez le prénom du deuxième étudiant : ")  
promo2 = input("Entrez la promotion du deuxième étudiant : ")  
group2 = input("Entrez le groupe du deuxième étudiant : ")  

etudiant2 = {  
    "name": name2,  
    "firstname": firstname2,  
    "promo": promo2,  
    "group": group2  
}  

# Étape 5 : Création du dictionnaire binôme  
binome = {  
    "id1": etudiant,  
    "id2": etudiant2  
}  

# Étape 6 : Affichage des membres du binôme  
print("\nLes étudiants formant le binôme sont :")  
for key, value in binome.items():  
    print(f"- L'étudiant {value['name']} {value['firstname']} du groupe {value['group']}.")