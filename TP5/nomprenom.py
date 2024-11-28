
nom1 = input("Entrez le nom de la première personne : ")  
prenom1 = input("Entrez le prénom de la première personne : ")  

nom2 = input("Entrez le nom de la deuxième personne : ")  
prenom2 = input("Entrez le prénom de la deuxième personne : ")  

personnes = [  
    (prenom1.capitalize(), nom1.upper()),  
    (prenom2.capitalize(), nom2.upper())  
]  
# Trier les personnes par nom, puis par prénom  
personnes.sort(key=lambda x: (x[1], x[0]))  

for prenom, nom in personnes:  
    print(f"{prenom} {nom}")
    