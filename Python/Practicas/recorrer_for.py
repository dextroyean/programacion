def run():
    nombre = input('Nombre:\n')
    for letra in nombre:
        print(letra)


    frase = input('Frase: ')
    for i in frase:
        print(i.upper())

if __name__ == '__main__':
    run()