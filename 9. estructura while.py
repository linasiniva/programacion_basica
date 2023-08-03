#************ESTRUCTURA WHILE *******************
"""n=int(input("ingrese un numero "))
contador=0
while contador != n:#iniciael ciclo con la  condicion
    contador=contador+1
    print(contador)"""
#////////////////////EJERCICIO 2//////////////////////
"""n=int(input("ingrese un numero,o -1 para salir"))
pares=0
impares=0
while n != -1:
    if n %2==0:
        print(" es par")
        pares+=1#forma de hacer un contador de mas 1
    else :
        print(" es impar")
        impares=impares+1#otra forma de hacer un contador de mas 1
    n=int(input("ingrese un numero entero, o -1 para salir "))
print("total pares: ",pares)
print("total impares: ",impares)"""
#*********************ESTRUCTURA DO WHILE ciclo infinito********************
"""#////////ejercicio de acensor que nunca pare///
while True:#crear un ciclo infinito
    opcion=int(input("elije un piso 1,2,3"))
    if opcion==1:
        print("moverse al piso 1")
    elif opcion==2:
        print("moverse al piso 2")
    elif opcion==3:
        print("moverse al piso 3")
    else:
        print("ERROR,ingrese una 1,2,3")"""
#//////////////EJERICIO/////////////

"""while True:#crear un ciclo infinito
    opcion=int(input("elije un piso 1,2,3"))
    if opcion==1:
        print("moverse al piso 1")
        break #rompemos el bucle se sale del ciclo 
    elif opcion==2:
        print("moverse al piso 2")
        continue #regresa al ciclo 
    elif opcion==3:
        print("moverse al piso 3")
    else:
        print("ERROR,ingrese una 1,2,3")"""
#//////////////////////////EJERICIO/////////////

#**************BLOQUE TRY(bloque try)except**********************
""""
while True:
    try:
        n1=int(input("ingrese numero"))
        n2=int(input("ingrese numero"))
        x=n1/n2
        print(x)
        break
    except:
        print("ERROR,elnumero debe ser intero")"""