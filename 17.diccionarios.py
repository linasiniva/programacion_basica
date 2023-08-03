#sentexis dediccionario
midiccionario={"id":1090231,"nombre":"ana","apellido":"sanchez",
"edad":20,"estatura":1.60,"parientes":["pedro sanchez","maria perez","juan sanzhez"]
,"salario":80000,"direccion":"calle20 bogota"}

#print(midiccionario)
#print(type(midiccionario))
#print(midiccionario["nombre"])#muestra el dato delnombre ejp ana
#print(midiccionario["edad"])# imprime 20
#print(midiccionario["parientes"])#['pedro sanchez', 'maria perez', 'juan sanzhez']
#print(midiccionario["parientes"][0:2])#memuestras 2 losdatos primeros ['pedro sanchez', 'maria perez']

#metodo agregar ,reemplazar y modificar un valor
"""
midiccionario["salario"]=1000000 #cambiar salario
print(midiccionario["salario"]) #imprime el cambio 1000000"""

#cambio de estructura modificar clave o cambiar 
"""
midiccionario["familia"]=midiccionario.pop("parientes")
print(midiccionario)"""

#agregar valor que no existe en diccionario
"""
midiccionario["estudia"]="ingenieria"
print(midiccionario)"""

#para eliminar (clave:valor) la etructura completa
"""
del(midiccionario["edad"])
print(midiccionario)#"""

#metodos get para diccionarios
"""
print(midiccionario["nombre"])#muestra dato ana

#print(midiccionario["hijo"])#KeyError: 'hijo' no esta en diccionario y se termina el programa
"""
"""
print(midiccionario.get("hijo","esta clave no esta en el diccionario"))#extraer o consultar y se obtiene msj si no existe
print(midiccionario.get("hijo"))#"""

#mostrar 2 valares del diccionario 
"""
print("{} {}".format(midiccionario["nombre"],midiccionario["salario"]))
"""
#mettodo para consultar solo claves y solo datos o valores
"""""
claves=midiccionario.keys()
print(claves)

valores=midiccionario.values()
print(valores)"""

#///////////////ejercicio///////////
capitales={"Venezuela":"Caracas","Colombia":"Bogota","Argentina":"Cordoba","Canada":"Ottawa",}

print(capitales)
print(capitales.get("medellin","Error "))
capitales["Argentina"]="Buenos aires"
print(capitales)
capitales["peru"]="lima"
capitales["Ecuador"]="quito"
print(capitales)

