from cmath import pi
"""import math
print(pi)
r=12
area=r*r*pi
print(area)"""
#///////////////////////
"""import math
print(dir(math))#funciones librerias """
#************LISTAS**********
#Sintaxis de listas"[] (lista vacia)
#Sintaxis de listas"[1,2,3] (lista llena)
#////////EJEMPLO DE LISTA/////////
"""nombre=[]#class lista
nombre2=()#class tuple
print(type(nombre2))"""
#/////////como moverme en la listas //////
"""nombre=["ana","pedro","maria"]
nunmeros=[1,2,3,4,5,6,7,8,9,20,15,26,11]
estatura=[1.60,1.55,1.80]
datos=[10,"isabella",1.50,3125632]
listavacia=[]

print(datos)#imprime lista
print(nombre[2])#me muestra el nombre en la posicion 02
print(nunmeros[0:8:2])#me muestra la lista de 2 en 2 hasta el 8
print(nunmeros[0:11:-1])#me muestra lista menos la ultima  posicion
print(nunmeros[:-2])#me muestra lista menos las 2 ultimas posiciones dela lista """
#///////////AGREGAR DATOS EN UNA LSTA //////////////

nombre=["ana","pedro","maria","ana","Ana","ANA"]
nunmeros=[1,2,3,4,5,6,7,8,9,20,15,26,11]
estatura=[1.60,1.55,1.80]
datos=[10,"isabella",1.50,3125632]
listavacia=[]

#*Metodo append agrega un elemento a una lista 
"""print(nombre)#imprime lista completa
nombre.append("diego")#agrega diego al final de la lista nombre 
print(nombre)#['ana', 'pedro', 'maria', 'ana', 'Ana', 'ANA', 'diego']"""
#*metodo extend 
"""listavacia.extend("bet")#agresa bet en la lista separando cada letra
print(listavacia)#['b', 'e', 't']"""
#*otro metodo extend con lista
"""estatura.extend(datos)#agrega lista dentro de otra al final
print(estatura)#[1.6, 1.55, 1.8, 10, 'isabella', 1.5, 3125632]
nombre.insert(1,25)#inserta el numero 25 en la posicion [01] de la lista nombre
print(nombre)#['ana', 25, 'pedro', 'maria', 'ana', 'Ana', 'ANA', 'diego']"""

#*metodo de pop elimanar un valor
"""nunmeros.pop()#sino coloco el numero de la posicion entonces al imprimir lista meelimina el ultimo valor
print(nunmeros)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 15, 26]
nunmeros.pop(0)#me elimina el primer numero q esta en la posicion 0
print(nunmeros)#[2, 3, 4, 5, 6, 7, 8, 9, 20, 15, 26]"""
#*metodo de remover para remover 
"""nombre.remove("pedro")#me quita de la lista a pedro
print(nombre)#['ana', 'maria', 'ana', 'Ana', 'ANA']"""
#*metodo para saber cuantos elementos tiene una lista 
"""contar=nunmeros.count(5)
print(contar)
print(nombre.count("ana"))
print(nombre.index("richard"))
 
tamano=len(nunmeros)#contar el tamaño o longitud de la lista/osea cuenta cada los elemnetos de la lista
print(tamano)
nordenados=sorted(nunmeros)#ordenar una lista 
print(nordenados)"""

#*metodo split()
"""txt="bienvenido a miision tic"
y= txt.split()
print(y)

a="hola mundo de mision tic"
x=a.split()#separa cada palabra con coma
print(x)#['hola', 'mundo', 'de', 'mision', 'tic']"""

#*metodo len
"""cant=len(a.split())#cuenta cada valor que hay en una lista=5
print(cant)#5"""
#////EJERCICIO////
#PROGRAMA
n=input("ingrese nombre completo fin  para salir")
#crear lista ,salida de programa
listanombre=[]
listapalabra=[]
while n != "fin" :#define lasalidad delciclo
    listanombre.insert(0,n)#inserta cada nombre agregado a la lista
    cant=len(n.split()) #cuenta la cantidad de palabra ingresada 
    listapalabra.insert(0,cant)#guarda la cantidad de palabras en la listapalabra
    n=input("ingrese nombre completo o fin para salir ")
print(listanombre)#imprime el nombre ingresado ['ana maria']
print(listapalabra)#imprime canntidad de nombre ana y maria osea = [2]"""
    




