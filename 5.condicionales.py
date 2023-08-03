#*************ESTRUCTURAS DE CONTROL: CONDICIONALES*************
"""#tipos de condicionales 
#/////////////////CONDICIONALES SIMPLES/////////////////
edad=int(input("ingrese por favor su edad: "))
if edad<18:
    print("usted no puede ingresar.Solo mayores de 18 años")"""

"""#/////////////////CONDICIONALES DOBLE/////////////////
edad=int(input("ingrese por favor su edad: "))
if edad<18:
    print("usted NO puede ingresar.Solo mayores de 18 años")
else:
    print("usted SI puede ingresar por se mayor de edad") """

"""#////////////////EJERCICIO 1  EN CLASES ////////////////

nombrEmpleado=(input("ingrese por favor su nombre: "))
salario=int(input("ingrese por favor su salario: "))

if salario<=1000000:
    print("El empleado {} TIENE DERECHO a subsidio de transporte,\nSu salario es de: ${:,} ".format(nombrEmpleado,salario+120000))
else:  
    print("El empleado {} NO TIENE DERECHO a subsidio de transporte,\nSu salario es de: ${:,} ".format(nombrEmpleado,salario)) """

#/////////////////CONDICIONALES MULTIPLES/////////////////   
"""#*******IF ANINADO***********
numero=int(input("ingrese un numeropor favor: "))
if numero>0:
    print("el numero es positivo")
elif numero <0:
    print("el numero es negativo")
else:
    print("el numero es un cero ")"""

"""#////////////////EJERCICIO 2  EN CLASES ////////////////

print("\t\tMENU\nElija una Opcion para saber su estacion \n ",1,2,3,4,sep=" \n Opcion ")
N=int(input())
if N==1:
    print("INVIERNO")
elif N ==2:
    print("VERANO")
elif N ==3:
    print("OTOÑO")
elif N ==4:
    print("PRIMAVERA")

else:
    print("\n*La opcion {} ingresado es INCORRECTA".format(N))"""    
#////////////////EJERCICIO 3  EN CLASES ////////////////

print("""\t\tMENU\nElija una Opcion para mostrar \n\n1 Suma\n2 Resta\n3 Multiplicar\n4 Dividir""")
N=int(input())
if N==1:
    N1=int(input("\nIngresar un numero: "))
    N2=int(input("Ingresar otro numero: "))
    rta=N1+N2
    print(f"*la suma de {N1}+{N2}= {rta} ")
elif N ==2:
    N1=int(input("\nIngresar un numero: "))
    N2=int(input("Ingresar otro numero: "))
    rta=N1-N2
    print(f"la resta de {N1}-{N2}= {rta} ")
elif N ==3:
     N1=int(input("\nIngresar un numero: "))
     N2=int(input("Ingresar otro numero: "))
     rta=N1*N2
     print(f"la multiplicacion de {N1}x{N2}= {rta} ")
elif N ==4:
    N1=int(input("\nIngresar un numero: "))
    N2=int(input("Ingresar otro numero: "))
    if N1==0 or N2==0:
        print("no se puede dividir con cero ")
    else:
            rta=N1/N2
            print(f"la division de {N1}/{N2}= {rta:0,.2f} ")
else:
    print(f"\n*La opcion {N} ingresado es INCORRECTA")
   
