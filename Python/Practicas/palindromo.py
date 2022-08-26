def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    inverso = palabra[::-1]
    if palabra == inverso:
        return True
    else:
        return False


def run():
    palabra = input('Ingresa la palabra: ')
    es_palindromo = palindromo(palabra)

    if es_palindromo == True:
        print('Es palindromo')

    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()