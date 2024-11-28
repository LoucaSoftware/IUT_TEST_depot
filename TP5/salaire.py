heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))  
salaire_horaire = float(input("Entrez le salaire horaire : "))  

# Calcul du salaire  
if heures_travaillees <= 160:  
    salaire = heures_travaillees * salaire_horaire  
else:  
    salaire = 160 * salaire_horaire  # Salaire pour les 160 premières heures  
    heures_sup_1 = min(heures_travaillees - 160, 40)  # Heures entre 161 et 200  
    salaire += heures_sup_1 * salaire_horaire * 1.25  # Majoré de 25%  
    
    heures_sup_2 = max(0, heures_travaillees - 200)  # Heures au-delà de 200  
    salaire += heures_sup_2 * salaire_horaire * 1.50  # Majoré de 50%  

# Afficher le salaire total  
print(f"Le salaire total est : {salaire:.2f} euros.")