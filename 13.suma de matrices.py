print("\t\t*****SUMA DE MATRICES*****")
filas = int(input ("Ingrese el Nº de filas de su matrices: "))
columnas = int(input ("Ingrese el Nº de columnas de su matrices: "))
matriz1 =[]
matriz2 =[]
matrizRESULTADO =[]
for f in range (filas):
	matriz1.append([0]*columnas)
	matriz2.append([0]*columnas)
	matrizRESULTADO.append([0]*columnas)
print ("\t Ingrese su Matriz 1")
for f in range(filas):
	for c in range(columnas):
		matriz1[f][c]=int(input("*Ingrese Nº en la posicion ({},{}):".format (f,c)))
print ("\t Ingrese su Matriz 2")
for f in range(filas):
	for c in range(columnas):
		matriz2[f][c]=int(input("*Ingrese Nº en la posicion ({},{}):".format (f,c)))
for f in range(filas):
	for c in range(columnas):
		matrizRESULTADO[f][c]=matriz1[f][c]+matriz2[f][c]
print ("* La suma de las matrices es:\n ",matrizRESULTADO)
