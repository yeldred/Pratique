class Personnage():

    def direBonjour(self,nom):
        print("Bonjour", nom)

    def chanter(self,paroles):
        print("je chante de lalalala....", paroles)


musicien = Personnage()
var = input("Entrer le nom de du personnage")
var1 = input("Entrer la chansons")
musicien.direBonjour(var)
musicien.chanter(var1)

