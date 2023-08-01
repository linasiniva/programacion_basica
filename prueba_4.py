def ordenar (listcodigo, listnombre,totalsiniva,totalconiva,N):
    if N>1:
        for i in range(N):
            for j in range(i+1,N):
                if listnombre[i]>listnombre[j]:
                    temp=listnombre[i]
                    listnombre[i]=listnombre[j]
                    listnombre[j]=temp
                    print(listcodigo[j])
                    print(listnombre[i])
                    print(totalsiniva[j])
                    print(totalconiva[j])
                    print(listcodigo[i])
                    print(listnombre[j])
                    print(totalsiniva[i])
                    print(totalconiva[i])  
    else:
        for i in range(i+1,N):
            print(listcodigo[i])
            print(listnombre[i])
            print(totalsiniva[i])
            print(totalconiva[i]) 
        
    return listcodigo, listnombre,totalsiniva,totalconiva,N
N=int(input())
ivatotal=0
totalfinal=0
listcodigo=[]
listnombre=[]
listcant=[]
listVunt=[]
listipoiva=[]
totalsiniva=[]
totalconiva=[]
iva=[]
for i in range(N):
    listcodigo.append(int(input()))
    listnombre.append(input())
    listcant.append(float(input()))
    listVunt.append(float(input()))
    listipoiva.append(int(input()))
    totalsiniva.append(listcant[i]*listVunt[i])
    if listipoiva[i]== 1:
        iva.append(0)
    elif listipoiva[i]==2:
        iva.append(totalsiniva[i]*0.05)
    elif listipoiva[i] ==3:
        iva.append(totalsiniva[i]*0.19)
    totalconiva.append(iva[i]+totalsiniva[i])
    totalfinal=totalfinal+totalconiva[i]
    ivatotal=ivatotal+iva[i]

ordenar(listcodigo, listnombre,totalsiniva,totalconiva,N)    
print(totalfinal)
print(ivatotal)