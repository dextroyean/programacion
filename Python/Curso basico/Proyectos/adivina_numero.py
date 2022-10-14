import random


def run():
    intentos = 1
    random_number = random.randint(1,100)
    choice = int(input('Elige un numero entre el 1 y el 100: '))

    while choice != random_number:
        intentos += 1
        if choice < random_number:
            choice = int(input('Elige un numero mayor: '))
        else:
            choice = int(input('Elige un numero menor: '))    
    print('Haz encontrado el numero secreto con', intentos, 'intentos')


if __name__ == '__main__':
    run()