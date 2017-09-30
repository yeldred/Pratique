#calcul le factoriel d'un nombre
"""

def factoriel(n):
    if(n == 0 or n == 1):
        return 1
    fact = 1
    for i in range(2,n+1):
        fact = fact * i
    return fact

print(factoriel(int(input("Entre la valeur factoriel"))))

"""
def factoriel(n):
    if(n == 0 or n == 1):
        return 1
    return n * factoriel(n-1)

print(factoriel(int(input("Entre la valeur factoriel"))))
