#****************VARIABLES DE CONTROL- ESTRUCTURAS ITERATIVAS**************
#///////////////ciclos FLOR (para)nos /////////////
#nos permite repetir hasta que el usuario lo permita
"""#imprimi de laposicion 0 al 2
for i in range(3):
    print(i)"""
"""#imprimi for donde empieza  en 2 hasta el 15, en 3 en 3
for i in range(2,15,3):
    print(i)"""
"""#imprimi for, donde empieza en 10 y disminuye hasta el 1, en 2 en 2
for i in range(10,1,-2):
    print(i)"""
"""#mostrar variables en ciclo for (imprime a 3 veces)
a="hola guapa "
for i in range(3):
    print(a)"""
"""#muestra el recorrido en for
for i in ["maria","felipe","jhon"]:
    print("hola",i) """

"""#mostrar 5 veces su nombre 
a=input("ingrese su nombre: ")
for i in range(5):  
    print(i+1,".",a) """
#//////////EJERCICIO TABLA DE MULTIPLICAR  /////////////
tab=int(input("\tingrese un numero del cual quiere saber la tabla\n"))
print("*LA TABLA DEL ",tab,"ES LA SIGUIENTE ")
for v in range (10):
    v=v+1
    print(v,"x",tab,"=",v*tab)

