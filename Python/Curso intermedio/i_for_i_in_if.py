def main():
    lista = []
    for i in range (1,10):
        if i % 3 != 0:
            lista.append(i**2)
    
    print(lista)

#esta condicion es igual a la anterior
#lista = [ i**2 for i in range(1, 10) if i % 3 != 0]


if __name__ == '__main__':
    main()