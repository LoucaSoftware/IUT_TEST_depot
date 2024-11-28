# Notes.py  

# Liste pour stocker les notes et coefficients  
notes = []  
coefficients = []  

# Demander à l'utilisateur d'entrer les notes et coefficients  
for i in range(1, 6):  
    entree = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")  
    note, coeff = map(float, entree.split())  # Séparer et convertir en float  
    notes.append(note)  
    coefficients.append(int(coeff))  # Convertir le coefficient en int  

# Calculer la moyenne générale  
somme_ponderee = sum(n * c for n, c in zip(notes, coefficients))  
somme_coefficients = sum(coefficients)  
moyenne = somme_ponderee / somme_coefficients if somme_coefficients > 0 else 0  

# Afficher la moyenne  
print(f"La moyenne générale est : {moyenne:.2f}")  

# Évaluer l'admission  
if moyenne >= 10 and all(n >= 8 for n in notes):  
    print("L'étudiant est admis.")  
else:  
    print("L'étudiant n'est pas admis.")
15