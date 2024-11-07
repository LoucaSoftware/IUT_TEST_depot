# Velo.py  

# Demander des heures de début et de fin de location  
debut = int(input("Donnez l’heure de début de la location (un entier) : "))  
fin = int(input("Donnez l’heure de fin de la location (un entier) : "))  

# Vérification des heures saisies  
if debut < 0 or debut > 24 or fin < 0 or fin > 24:  
    print("Les heures doivent être comprises entre 0 et 24 !")  
elif debut == fin:  
    print("Attention ! l’heure de fin est identique à l’heure de début.")  
elif debut > fin:  
    print("Attention ! le début de la location est après la fin ...")  
else:  
    # Initialisation des variables pour calculer le coût  
    tarif1_duration = 0  # Durée à 1 euro  
    tarif2_duration = 0  # Durée à 2 euros  
    montant_total = 0.0  

    # Calcul des durées pour chaque tarif  
    for heure in range(debut, fin):  
        if (0 <= heure < 7) or (17 <= heure < 24):  
            tarif1_duration += 1  
            montant_total += 1.0  # 1 euro par heure  
        else:  
            tarif2_duration += 1  
            montant_total += 2.0  # 2 euros par heure  
    
    # Affichage des résultats  
    print("Vous avez loué votre vélo pendant")  
    if tarif1_duration > 0:  
        print(f"{tarif1_duration} heure(s) au tarif horaire de 1.0 euro(s)")  
    if tarif2_duration > 0:  
        print(f"{tarif2_duration} heure(s) au tarif horaire de 2.0 euro(s)")  
    
    print(f"Le montant total à payer est de {montant_total:.1f} euro(s).")