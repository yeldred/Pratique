"""
fin = 5
a = 0

while(a <= fin):
    a += 1
    result = " # " * a
    print(result)
"""
#fin+++++++++
"""
#programme declaration d'amour

import  random
import time

reponseFile = random.randrange(0,2)

print("Est-ce que tu m'aime ? :")
time.sleep(3)

if reponseFile == 0:
    print(" je ne t'aime pa du tout, bien au contraire je te deteste ")
else:
    print("Je t'aime plus que tout au monde, et cela depuis ma naissance ")
#fin+++++++++++++
"""
"""
# jeu de plus ou moins
import  random
print("++++++Jeu de plus ou moins+++++++++++\n\
      Je viens de penser a un nombre entre 1 et 100.\nDevines lequel ? ")

nbreAleatoire = random.randrange(1,100)

while(True):
    print("votre valeur ?")
    nbreEntrer = int(input())

    if(nbreAleatoire > nbreEntrer):
        print("votre nombre est trop petit")
    elif(nbreAleatoire < nbreEntrer):
        print("votre nombre est trop grand")
    else:
        print("Bingo")
        break

"""
from math import fabs

print(int(fabs(-23)))