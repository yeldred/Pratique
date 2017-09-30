"""ma_chaine = "Bonjour"

ma_chaine = ma_chaine.capitalize()

print(ma_chaine)"""
inven = []
print(inven[:])
val1 = input("entrer une l'information du liste")
while val1 != "quit":

    inven.append(val1)
    val1 = input("entrer une l'information du liste")

print(inven[:])
val2 = input("entrer une le valeur a changer")
val3 = input("entrer une l'information du liste")
val4 = inven.index(val2)

inven[val4] = val3
print(inven[:])
print(inven.count())

