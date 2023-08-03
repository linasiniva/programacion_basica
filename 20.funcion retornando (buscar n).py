def buscarn(numeros,buscar):#busca un vaolor en una lista y retorna la posicion en memoria o la ubicacion de ese valor
    for i in range(len(numeros)):#busca linalmente con lalongutid de la lista 
        if buscar== numeros[i]:
            #print("si se encuentra ",i)
            return i
            
    else:
        return -1
       

numeros=[2,4,1,5,3,10]
buscar=5

resultado=buscarn(numeros,buscar)   

if resultado==-1:
    print("no se encuentra")
else:
    print("encontrado en ",resultado)
#print(resultado)
