#*********************VARIABLES**********************
#variable tipo entero
a=5 
#variable tipo flota /flotante osea decimal
b=5.2 
#variable tipo string
c="hola mundo"
#variable tipo booleano
d=True
#tipo de dato diccionario
e={}
#tipo de dato tuple 
f=()
#tipo de dato lista 
g=[]
#para saber tipo de dato 
type(a)
#para imprimer el tipo de 
#dato asociado a la varible dentro de parentisis
print(type(g))
#******************MOSTRAR EN PANTALLA******************
#Mostrar en pantalla texto 
print("hola mundo\n")
#salto de linea en un texto \n
print("para imprimir un parrafo","\nsegundo parrafo en la linea de abajo")
#imprimir lista puede se numerica o alfa numerica 
print(1,2,3,4,5,6) #en una solo lina imprimi lista 
print(7,8,9,10,sep="\n")#imprime un numero abajo del otro atraves de salto de linea 
#imprimir un menu
print("primero","segundo","tercero",sep="\n")# sep es un separador (variable) q se utiliza para guardar elsalto de linea->\n
"""para comentar varias linas se utiliza con 3 comillas
al principio y 3 comillas aloultimo """
#otra forma de imprimir un menu
print("""
1 ingresar
2 salir
3 guardar
4 cambiar""")
#otra forma de imprimir menu 
Menu=("""
1 ingresar
2 salir
3 guardar
4 cambiar""")#variable de tipo string
print(Menu)#imprimimos variable menu
