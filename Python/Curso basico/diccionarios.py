diccionario = {
    "nombre": "Arya",
    "raza": "Husky",
    "edad": 9
}

print(diccionario)

perro = diccionario.copy()

print('nombre:', diccionario["nombre"]) #metodo 1 de consulta de un diccionario
print('raza:', diccionario.get('raza')) #metodo 2 de consulta de un diccionario

diccionario['edad'] = 10  #como modificar un valor de un diccionario

print(diccionario, "elementos en dic:",len(diccionario))

diccionario["ladra"] = "si" #agrega elementos a un diccionario
print(diccionario)

diccionario.pop("ladra") #elimina un campo del dic
print (diccionario)

del diccionario["edad"] #otro metodo para eliminar
print(diccionario)
print(perro)

for valores in diccionario.keys():
    print(valores)  #con .keys accedemos al nombre de las variables en el diccionario

for valores in diccionario.values():
    print(valores) #.values sirve para acceder a lso valores de las variables