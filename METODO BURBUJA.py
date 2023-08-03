#ordenar de mayor a menor
def llenar(lista,n):
    for i in range(n):
        valor=input("ingrese un valor a la lista")
        lista.append(valor)
    return lista

def ordenar(lista,n):#de menor a mayor los valores de la lista 
    for i in range(n):
        for j in range(i+1,n):
            if lista[i]>lista[j]:
                temp=lista[i]
                lista[i]=lista[j]
                lista[j]=temp
    return lista

def ordenarinv(lista,n):#de mayor a menor  los valores de la lista 
    for i in range(n):
        for j in range(i+1,n):
            if lista[i]<lista[j]:
                temp=lista[i]
                lista[i]=lista[j]
                lista[j]=temp
    return lista


lista=[]
n=int(input("ingrese cantidad del elemento de la lista"))
lista2=llenar(lista,n)
print(lista)
lista3=ordenar(lista,n)#de menor a mayor los valores de laa lista 
print(lista3)
lista4=ordenarinv(lista,n)#de mayor a menor
print(lista4)