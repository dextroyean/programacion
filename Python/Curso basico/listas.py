lista = [8,2,3,]
print(lista)

lista.append(4) #agrega elementos
print(lista)

lista2 = lista.copy() #copia lista

lista.clear() #limpia lista
print(lista, lista2)

LargoLista = len(lista2) #len cuenta los elementos en una lista
print(LargoLista) 

lista2.remove(2) #elimina un registro en concreto
print(lista2)

lista2.sort() #ordena los elementos, tienen que ser del mismo tipo de dato
print(lista2)

lista2.pop() #elimina el ultimo registro de una lista
print(lista2)


rango = range(8) #crea un rango numerico
print(rango)




#las tuplas son la misma estructura pero con una lectura mucho mas rapida que las listas, con la diferencia que estas no se pueden modificar.
mi_tupla = (1,2,3,4,5)
print(mi_tupla)