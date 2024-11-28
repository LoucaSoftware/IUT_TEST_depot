def est_bissextile(annee):  
    """Détermine si une année est bissextile."""  
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)  

def verification_date(date_str):  
    """Vérifie si la date est valide au format jjmmaaaa."""  
    
    # Vérification du format  
    if len(date_str) != 8 or not date_str.isdigit():  
        return "Format incorrect. Veuillez entrer une date au format jjmmaaaa."  

    # Extraction des éléments de la date  
    jour = int(date_str[:2])  
    mois = int(date_str[2:4])  
    annee = int(date_str[4:])  

    # Vérification des mois  
    if mois < 1 or mois > 12:  
        return "Mois invalide. Veuillez entrer un mois entre 01 et 12."  
    
    # Vérification des jours par mois  
    jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    
    # Ajustement pour les années bissextiles  
    if est_bissextile(annee):  
        jours_par_mois[1] = 29  # Février a 29 jours en année bissextile  

    # Vérification du jour  
    if jour < 1 or jour > jours_par_mois[mois - 1]:  
        return f"Jour invalide pour le mois {mois}. Veuillez entrer un jour valide."  

    return "La date est valide."  


date_input = input("Entrez une date au format jjmmaaaa : ")  
message = verification_date(date_input)  
print(message)