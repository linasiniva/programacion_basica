#/////////////FUNCIONES/////////////
"""
def sumar(a,b):#funcion con 2 parametros a,b
    #suma 2 valores
    #c=a+b
    #return c
    return a+b

resultado=sumar(20,30)#envios estos argumentos para que sumeesos 2numeros
#resultado=sumar(b=20,a=30)
print(resultado)#"""

#///////////////


def restar(a=None,b=None):
    if a==None or b==None:
        error="debe ingresar 2 valores"
        return error
    else:
        c=a-b
        return c
resultado=restar(2,3)
print(resultado)

#/////////CALCULADORA DE FUNCIONES//////
# Hacer una calculadora, que solicite 2 números,
# y resuelva operaciones básicas con funciones definidas por el usuario

print("\t\tMENU\nElija una Opcion para mostrar \n\n1 Suma\n2 Resta\n3 Multiplicar\n4 Dividir")
N=int(input())

def sumar(a=None,b=None):
    if a==None or b==None:
        error="debe ingresar 2 valores"
        return error
    else:
        c=a+b
        return c

def restar(a=None,b=None):
    if a==None or b==None:
        error="debe ingresar 2 valores"
        return error
    else:
        c=a-b
        return c

def multiplicar(a=None,b=None):
    if a==None or b==None:
        error="debe ingresar 2 valores"
        return error
    else:
        c=a*b
        return c   

def dividir(a=None,b=None):
    if a==None or b==None:
        error="debe ingresar 2 valores"
        return error
    else:
        c=a/b
        return c     

n1=int(input("ingrese un numero "))
n2=int(input("ingrese otro numero "))
if N==1:
    resultado=sumar(n1,n2)
    print(resultado)

if N==2:
    resultado=restar(n1,n2)
    print(resultado)

if N==3:
    resultado=multiplicar(n1,n2)
    print(resultado)

if N==4:
    resultado=dividir(n1,n2)
    print(resultado)

#///////////////FUNCION CON MAIN////////////////////////////////

def palabras():
    #recibe un texto del teclado
    palabras=input("escriba palabra")
    
    return palabras

    if __name__=="_main_":
        palabras()


