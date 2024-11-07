# Intervalle.py  
# Ce programme teste l'appartenance d'un nombre réel à l'intervalle I.  

# Demande à l'utilisateur d'entrer un réel  
x = float(input("Entrez un nombre décimal : "))  

# Vérification de l'appartenance à l'intervalle I  
appartient_ensemble_I = (  
    (x >= 2 and x < 3) or   # Intervalle [2,3[  
    (x > 0 and x <= 1) or   # Intervalle ]0,1]  
    (x >= -10 and x <= -2)  # Intervalle [-10,-2]  
)  

# Affichage du résultat  
if appartient_ensemble_I:  
    print("x appartient à I")  
else:  
    print("x n'appartient pas à I")