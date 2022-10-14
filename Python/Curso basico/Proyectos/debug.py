import random

MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
passwolrd = []

def asignar_caracter(tipo):
    longitud = len(tipo)
    rando = random.randint(0,longitud) - 1
    caracter = tipo[rando]
    passwolrd.append(caracter)    

asignar_caracter(MAYUS)
print(passwolrd)


