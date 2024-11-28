# # Palindrome.py  

# def est_palindrome(chaine):  
#     # Retirer les caractères non alphabétiques et mettre en minuscules  
#     chaine_epuree = ''.join(c.lower() for c in chaine if c.isalpha())  
    
#     # Vérifier si la chaîne épurée est égale à son inverse  
#     return chaine_epuree == chaine_epuree[::-1]  

# # Programme principal  
# if __name__ == "__main__":  
#     chaine = input("Entrez un mot ou une phrase : ")  
    
#     if est_palindrome(chaine):  
#         print("C'est un palindrome !")  
#     else:  
#         print("Ce n'est pas un palindrome.")



# chaine = input("Entrez un mot ou une phrase : ")  

# # conserver uniquement les lettres en minuscules  
# chaine_epuree = ''.join(c.lower() for c in chaine if c.isalpha())  


# if chaine_epuree == chaine_epuree[::-1]:  
#     print("C'est un palindrome !")  
# else:  
#     print("Ce n'est pas un palindrome.")






















# #Palyndrome.py 
# #sans les deux chaines à mettre dans le programme que sous la forme d'une seule



# def palindrome_2(chaine):  
#     # Retirer les caractères non alphabétiques et mettre en minuscules  
#     chaine_epuree = ''.join(c.lower() for c in chaine if c.isalpha())  
    
#     # Vérifier si la chaîne épurée est égale à son inverse  
#     return chaine_epuree == chaine_epuree[::-1]  

# while () {


# }



# if __name__ == "__main__":  
#     chaine = input("Entrez un mot ou une phrase : ")  
    
#     if est_palindrome(chaine):  
#         print("C'est un palindrome !")  
#     else:  
#         print("Ce n'est pas un palindrome.")



# chaine = input("Entrez un mot ou une phrase : ")  

# # conserver uniquement les lettres en minuscules  
# chaine_epuree = ''.join(c.lower() for c in chaine if c.isalpha())  


# if chaine_epuree == chaine_epuree[::-1]:  
#     print("C'est un palindrome !")  
# else:  
#     print("Ce n'est pas un palindrome.")




# Palindrome.py VERSION 2 AVEC BOUCLE WHILE: 

def palindrome(chaine):  
    #i , j deux indices pour désigner le début et la fin de la chaine
    # Retirer les caractères non alphabétiques et mettre en minuscules  
    i = 0
    j = len(chaine) - 1  
    
    #entrer dans la boucle et comparaison des lettre respectivement i pour aller à DROITE
    #j pour aller à GAUCHE en diminuant l'indice
    while i < j:  
        # Caractère à gauche  
        while i < len(chaine) and not chaine[i].isalpha(): #rentre dans la boucle pour augmenter i  
            i += 1  
        
        # Caractère à droite  
        while j >= 0 and not chaine[j].isalpha():  #rentre dans la boucle pour augmenter j
            j -= 1  
            
        # caractères en minuscules  
        if chaine[i].lower() != chaine[j].lower():   
            return False  
          
        i += 1  
        j -= 1  
    
    return True  

# Programme principal  
if __name__ == "__main__":  
    chaine = input("Entrez un mot ou une phrase : ")  
    
    if palindrome(chaine):  
        print("C'est un palindrome !")  
    else:  
        print("Ce n'est pas un palindrome.")



# Palindrome.py VERSION 2 AVEC BOUCLE WHILE et utilisation des propriété de n à n-1 sans la copie de la chaine pour:
# OPTIMISATION DU CODE


def palindrome(chaine):  
    #i , j deux indices pour désigner le début et la fin de la chaine
    # Retire les caractères NON alphabétiques et mettre en minuscules  
    i = 0
    j = len(chaine) - 1  
    
    #entrer dans la boucle et comparaison des lettre respectivement i pour aller à DROITE
    #j pour aller à GAUCHE en diminuant l'indice
    while i < j:  
        # Caractère à gauche  
        while i < len(chaine) and not chaine[i].isalpha(): #rentre dans la boucle pour augmenter i  
            i += 1  
        
        # Caractère à droite  
        while j >= 0 and not chaine[j].isalpha():  #rentre dans la boucle pour augmenter j
            j -= 1  
            
        # caractères en minuscules  
        if chaine[i].lower() != chaine[j].lower():   
            return False  
          
        i += 1  
        j -= 1  
    
    return True  

# Programme principal  
if __name__ == "__main__":  
    chaine = input("Entrez un mot ou une phrase : ")  
    
    if palindrome(chaine):  
        print("C'est un palindrome !")  
    else:  
        print("Ce n'est pas un palindrome.")