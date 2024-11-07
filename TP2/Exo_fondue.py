# Fondue.py  

# Déclaration des constantes et des variables de base  
BASE = 4  # Nombre de personnes pour la recette de base  
fromage = 800.0  # Quantité de fromage en grammes pour BASE personnes  
eau = 2  # Quantité d'eau en décilitres pour BASE personnes  
ail = 2  # Nombre de gousses d'ail pour BASE personnes  
pain = 400  # Quantité de pain en grammes pour BASE personnes  

# Demande à l'utilisateur d'introduire le nombre de convives  
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))  

# Adaptation des quantités en fonction du nombre de convives  
fromage_adapte = fromage * nbConvives / BASE  
eau_adapte = eau * nbConvives / BASE  
ail_adapte = ail * nbConvives / BASE  
pain_adapte = pain * nbConvives / BASE  

# Affichage de la recette pour le nombre de convives voulu  
print(f"\nPour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")  
print(f"- {fromage_adapte:.1f} gr de fromage")  
print(f"- {eau_adapte:.1f} dl d'eau")  
print(f"- {ail_adapte:.1f} gousse(s) d'ail")  
print(f"- {pain_adapte:.1f} gr de pain")