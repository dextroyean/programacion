import random

def gen_pass():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    passworld = []

    def asignar_caracter(tipo):
        longitud = len(tipo)
        rando = random.randint(0,longitud) - 1
        caracter = tipo[rando]
        passworld.append(caracter)    


    for i in range(10):
        random_number = random.randint(1,4)
        if random_number == 1:
            asignar_caracter(MAYUS)
        elif random_number == 2:
            asignar_caracter(MINUS)
        elif random_number == 3:
            asignar_caracter(NUMS)
        else:
            asignar_caracter(CHARS)
    passworld = "".join(passworld)
    return passworld

def run():
    passworld = gen_pass()
    print('Tu contraseña es:', passworld)


if __name__ == '__main__':
    run()