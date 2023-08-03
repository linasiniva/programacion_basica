"""#******************FORMATEO DE SALIDAS****************
#formateo de int 
numero=452698214
print("{:,}".format(numero)) 

#formateo de float
numero2=1256.25497
print("{:,.2f}".format(numero2))

# NOTA: lo que se utiliza en corchete {:,} es para la separacion de 
# puntuacion de miles y millones ejp: 452,698,214 de la variable numero 
# y esta {:,.2f} el .2f es pa cantidad de decimales despues del
# punto ejp: 1256.25 de la variable numero2 

#otra forma de formateo 
n=548.25624
print(f"{n:,.2f}")#para mostrar 548.26 n con solo 2 decimales 
print(f"{1200:,.2f}")#Añadiendo un numero directamente y no con varible y mostrando 2 decimales
print(f"{1200:,}")#Añadiendo un numero directamente realizando la separacion de decimales  

#formateo con valor ingresado 
n2=int(input("ingrese valor: "))
print(f"{n2:,.2f}")"""

"""#******************FORMATEO DE ENTRADAS***************** 

#Ingresar parametros con format()
print("mi nombre es {} {} gracias por {}".format("lina","siniva","venir"))#loscorchetes se reemplazan por las palabras dentro de format

#otra forma de formateo de entrada 
nombre=input("cual es su nombre?: ")
apellido=input("cual es su apellido?: ")
x="venir"
print("Bienvenido  {} {} gracias por {}".format(nombre,apellido,x))

#forma corta de formateo de entrada
print(f"Hola  {nombre} {apellido} gracias por {x}")"""
"""
#otra forma de formateo de entrada
print("hola como estas tripulante {} {}".format(input("ingrese su primer apellido :"),input("ingrese su segundo apellido : ")))"""

"""#************OPERADORES DE PERTENCIA*******************
# in y not : son operadores de pertenencia
# in : devuelve true si el valor especificado se encuentra en la secuencia.En caso contrario devuelve False
# not in : devuelve true si el valor especificado no se encuentra en la secuencia.En caso contrario devuelve False

Cadena="Hola Mundo"
print("Mundo" in Cadena )#true
print("mundo" in Cadena )#false
print("codigo" not in Cadena )#true

#*************OPERADORES DE IDENTIDAD*******************
a,b =3,3
c=4
print(a is b)#True
print(a is not  b)#False
print(a is not c)#True
#/////////////////////////
x=1
y=x
z=y
print(z is 1)#muestra True
print(z is x)#muestra True
#/////////////////////////
cadena1,cadena2="UNAB","UNAB"
print(cadena1 is cadena2)#True
print("UPA" is cadena2)#False
#/////////////////////////
r= [10,20,30]
s= [10,20,30]
print(r is s)# False listas obj mutables """

#*****************VARIABLES Y EXPRESIONES ***************
minombre="Hola,Richard"
print("mi nombre es: ",minombre)
print(minombre.upper())#esta linea convierte pasa todo a MAYUSCULA
print(minombre.lower())#cambia las letras que esten en mayusculas a MINISCULAS
print(minombre.swapcase())#cambia las letras que esten en minisculas a MAYUSCULAS
print(minombre.capitalize())#Deja en el texto solo la primera letra que inicie con MAYUSCULA el resto del texto en miniscula
print(minombre.count("r"))#muestra cuantas veces se repite r en la variable minombre de loque esta en comillas
print(minombre.find("a"))#posicion de la primera a
print(minombre[6])
print(minombre.replace("d","dito"))#reemplaza laletra d por la dito 
print(minombre.replace("Hola","Chao"))#cmbia palabra por otra palabra