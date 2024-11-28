

# Demande le nombre d'étudiants à l'utilisateur  
nombreEtudiants = int(input("Donnez le nombre d'étudiants : "))  
moyenne = 0.0  
notes = []  

# Remplissage de la liste avec les notes des étudiants  
for i in range(nombreEtudiants):  
    while True:  
        note = float(input(f"Note étudiant {i} : "))  
        if 0 <= note <= 20:  
            notes.append(note)  
            break  
        else:  
            print("la note doit être comprise entre 0 et 20.")  

# Calcul de la somme des notes  
sommeNotes = sum(notes)  

# Calcul de la moyenne  
moyenne = sommeNotes / nombreEtudiants  

# Affichage de la moyenne  
print(f"Moyenne de classe : {moyenne:.2f}")  

# Affichage des écarts à la moyenne  
print("\nNuméro de l’étudiant | Note | Écart à la moyenne")  
for i in range(nombreEtudiants):  
    ecart = notes[i] - moyenne  
    print(f"{i} | {notes[i]} | {ecart:.2f}")