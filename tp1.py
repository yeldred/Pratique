# tp1

"""
nomUser = input("Quel est ton nom ? ")
print(nomUser)

"""
#finn++++++++++++++++++++++


#tp2 casting
"""
int('23')---chaine de caractere en entier
int(23.0)---decimal en entier
str(23)----entier en chaine de caractere
"""

"""
nombre1 = input("Entrer le premier nombre : ")
nombre1 = int(nombre1)
nombre2 = input("Entrer la deuxieme nombre : ")
nombre2 = int(nombre2)
somme = nombre1 + nombre2
print(somme)

#fin+++++++++++++++++++++++++++++++++++++
"""



#tp2 programme simulant un baby-sitter en quete d'emploie
"""
print("Hello madame")

nbrEnfants = input("combien d'enfant avez-vous :")
nbrEnfants = int(nbrEnfants)

if(nbrEnfants == 1):
    print("Je veux etre la babysitter de votre enfant")
elif(nbrEnfants > 1):
    print("Je veux etre la baby-sitter de vos enfants")
else:
    print("Merci desole de vous avoir derange ")

#fin+++++++++++++++++++++++
"""

"""
#tp3 boucle

#boucle while
debut = input("entrer la valeur de depart : ")
debut = int(debut)
fin = input("entrer la valeur a arrete : ")
fin = int(fin)
fin += 1

while(debut <= fin):
    print(debut)
    debut += 1
#fin++++++++++++++++++


#boucle for
for x in range(debut,fin):
    print(x)
"""

def estPair(nbre):
    """     Fonction permettant de savoir si le nombre fourni est pair ou non """
    if(nbre % 2 == 0):
        return True
    else:
        return False

nbre = int(input("Entre le nombre de votre choix"))
print(estPair(nbre))




