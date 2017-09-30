
class Humain:

    def __init__(self, c_nom,c_age ):
        self.nom = c_nom
        self.age = c_age


print("lancement du programme")
nom_entrer =input("Entrer le nom")
age_entrer =input("Entrer l'age de l'enfant")
h1 = Humain(nom_entrer,age_entrer)

print(" le nom de l'enfant est {} et de l'age {}".format(h1.nom,h1.age))
