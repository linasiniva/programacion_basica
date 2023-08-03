"""lista=[1,2,5,"b","hola",True,[1,2,3]]

print(lista)
print(type(lista))

print(lista[6])"""

#//////////////////LISTAS DENTRO DE LISTAS(MATRICEZ)////////////////////////
#listasdelistas=[[1,2,3],[4,5,6],[7,8,9]]
"""print(listasdelistas)#muestra lista [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listasdelistas[2])#muestra la fila 2[7, 8, 9]
print(listasdelistas[0][1])#muestra elnumero dela posicion 01 = 2"""

#/////mostrar matriz//////
"""for i in range(0,3):
    print(listasdelistas[i])#imprime lista de 3x3
    # [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]"""
#//////////////////matriz longitud listas imprime solo filas /////////////    
"""listasdelistas=[[1,2,3],[4,5,6],[7,8,9],[10,11,12,13]]
for i in range(len(listasdelistas)):
    print(listasdelistas[i])
    #[1, 2, 3]
    #[4, 5, 6]
    #[7, 8, 9]
    #[10, 11, 12, 13]"""
#//////////////MUESTRA FILA HORIZONTAL Y LUEGO VERTICAL////////////
"""listasdelistas=[[1,2,3],[4,5,6],[7,8,9]]

for fila in range(len(listasdelistas)):
    print(listasdelistas[fila])
    for columna in range(0,3):
        print(listasdelistas[fila][columna])"""
#//////// MATRIZ////////
"""listasdelistas=[["ana",2,3],["juan",5,6],["pedro",8,9]]
for fila in range(len(listasdelistas)):
    print(listasdelistas[fila])
    for columna in range(0,3):#en rango siempre me va a sumar 1 mas 
        print(listasdelistas[fila][columna])  """
#//////////ejercicio matriz/////////////

"""lista=[]
for fila in range(2):
    lista.append([])
    #print(lista)
    for columna in range(2): 
        n=int(input("ingrese numero "))
        lista[fila].append(n)
        print(lista)"""
       
#///////////////////ejercicio ejemplo ///////////

"""lista=[["ana",15,"a"],["juan",20,"j"]]
vacia=[]
for fila in lista:
    vacia.append(fila[1])#[15, 20]
print(vacia)"""
#///////////////////ejercicio ejemplo suma de matrices ///////////

x=[[12,2,5],[2,5,8],[6,9,4]]
y=[[2,6,7],[4,5,7],[20,4,7]]
rta=[[0,0,0],[0,0,0],[0,0,0]]

for f in range(3):
    for c in range(3):
        rta[f][c]=x[f][c]+y[f][c]
print(rta)





        
   