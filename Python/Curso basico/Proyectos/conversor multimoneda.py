pesos = 1
dolar = 19.92
euro = 20.26 
resultado = 0


menu = """
Elige una opción: 

1.- De Peso a Dolar
2.- De Peso a Euro
"""
moneda = input(menu)

def conversor (denominacion):
    cantidad = float(input('Ingresa la cantidad de pesos a convertir: '))
    resultado = cantidad / denominacion
    resultado = str(round(resultado,2))
    cantidad = str(round(cantidad, 2))
    return cantidad
    return resultado


if moneda == '1':
    conversor(dolar)
    print("$" + cantidad + " de pesos a dolares son: $" + resultado)

else:
    cantidad = float(input('Ingresa la cantidad de euros a convertir: '))
    resultado = cantidad  / euro
    resultado = str(round(resultado,2))
    cantidad = str(round(cantidad, 2))
    print("$" + cantidad + " de pesos a euro son: $" + resultado)

