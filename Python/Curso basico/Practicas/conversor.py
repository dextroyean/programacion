menu = """
Elige una opción: 

1-De pesos a dolar
2-De dolar a pesos

"""
moneda = input(menu)

pesos = 1
dolar = 20.27
resultado = 0


if moneda == '1':
    cantidad = float(input('Ingresa la cantidad de pesos a convertir: '))
    resultado = cantidad / dolar
    resultado = str(round(resultado,2))
    cantidad = str(round(cantidad, 2))
    print("$" + cantidad + " de pesos a dolares son: $" + resultado)

else:
    cantidad = float(input('Ingresa la cantidad de pesos a convertir: '))
    resultado = cantidad * dolar
    resultado = str(round(resultado,2))
    cantidad = str(round(cantidad, 2))
    print("$" + cantidad + " de dolares a pesos son: $" + resultado)

