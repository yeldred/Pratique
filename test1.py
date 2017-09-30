"""nomTexte = "Hello world \n thats good"
print(nomTexte)

for val1 in range(20):
    val1 += 1
    print(val1)

valeur1 = "Bonjour"

var1 = (valeur1[1:3])
var2 = (valeur1[3:5])

print(var1 + var2)
valeur2 = input("entrer le premier valeur")
valeur2 = int(valeur2)
valeur3 = input("entrer la dexieme valeur")
valeur3 = int(valeur3)
resultat = (valeur2 + valeur3)

print("le resultat est :,",resultat)

"""

print("--------------------")
"""
identifiant = "jason"
mot_De_Passe = "password"

user_id = input("Entrez votre identifiant: ")
user_password = input("Entrez votre mot de passe :")

if (user_id == identifiant) and (user_password == mot_De_Passe):
    print("Vous etes connectes, bienvenue", user_id)
else:
    print("identifiant ou mot de passe incorrect")
"""

"""
identifiant = "jason"
mot_De_Passe = "password"

user_id = input("Entrez votre identifiant: ")
user_password = input("Entrez votre mot de passe :")

while (user_id != identifiant)or (user_password != mot_De_Passe):
    print("identifiant ou mot de passe incorrect")
    user_id = input("Entrez votre identifiant: ")
    user_password = input("Entrez votre mot de passe :")

print("Vous etes connectes, bienvenue", user_id)
"""
"""
valeurPair = input("Enterz un valuer pair svp :")

valeurPair = int(valeurPair)

while( valeurPair % 2 ):
    valeurPair = input("Enterz un valuer pair svp :")
    valeurPair = int(valeurPair)

print("La valeur entrez est : ", valeurPair)

"""
"""
jeuLancer = True

print(" ")

while jeuLancer:
    choixMenu = input(">")
    if choixMenu == "again":
        continue
    elif choixMenu == "hello":
        print("Bonjour")
    elif choixMenu == "quit":
        jeuLancer = False
print("end")
"""

nom = input("Enter le nom")
prenom = input("Entrer le prenom: ")

def info(nom,prenom):
    print(" le nom est {} et le prenom est {}".format(nom,prenom))

info(nom,prenom)