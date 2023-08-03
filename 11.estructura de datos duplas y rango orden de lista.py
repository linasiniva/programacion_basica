#*********************DUPLAS**************************************
tupla=(1,2,3,4)
tuplan=("a","b","c")
tuplanombre=("ana","juan","pedro","ana","Ana")
tuplamas=(10,2.5,"hola")
lista=[1,2,3,4,6,8,9,10]
"""print(tupla)
print(lista)"""

"""lista.append("any")
print(lista)
#agregar elemento a la tupla no se puede porq es imutableno se puede cambiar
contar=tuplanombre.count("ana")
print(contar)
#mostrar en que direccion encuentro el elemento
print(tuplanombre.index("juan"))#me muestra laposicion donde esta juan en posicion 01
#mostrar posicion de una memoria""" 

"""
print(tupla[2:])#(3, 4)
print(lista[3:])#[4, 6, 8, 9, 10]
print(lista[1:8:2])#[2, 4, 8, 10]"""
#***************RANGOS************
#Definiendo rango
"""print(range(5))#range(0, 5)
print(range(1,5))#range(1, 5)
print(range(1,5,2))#range(1, 5, 2)"""

#//////ejercicio////////
#transformacion de rango a lista
"""print(list(range(5)))#[0, 1, 2, 3, 4]
print(list(range(1,15)))#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12, 13, 14]
print(list(range(1,15,2)))#[1, 3, 5, 7, 9, 11, 13]"""

"""print(type(tupla))
print(tuple(range(5)))
print(tuple(range(1,5)))"""
#variable con tupla generada por un rango 
"""vari=tuple(range(1,15,2))
print(vari)"""
#****************ORDENAR UNA LSTA*************
lista=[0,25,1,4,8,6,36,9,11, 1, 2, 3, 4]
listaordenada=sorted(lista)#ordenar de menor a mayor
listaacendente=sorted(lista,reverse=True)#ordenar de mayor a menor
print(lista)
print(listaordenada)
print(listaacendente)
#////////////////


