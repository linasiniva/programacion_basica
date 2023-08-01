def ordenar (listcodigo, listnombrearticulo,totalsiniva,totalconiva,N):# se define una funcion en python para ordenar las listas
    if N>1:# se hace un condicional donde la cantidad de articulos sea mayor de 1
        for i in range(N):#se realiza un metodo burbuja par ordenar la lista de menor a mayor
            for j in range(i+1,N):
                if listnombrearticulo[i]>listnombrearticulo[j]:
                    temp=listnombrearticulo[i]
                    listnombrearticulo[i]=listnombrearticulo[j]
                    listnombrearticulo[j]=temp
                    print(listcodigo[i])
                    print(listnombrearticulo[j])
                    print(totalsiniva[i])
                    print(totalconiva[i])
                    print(listcodigo[j])
                    print(listnombrearticulo[i])
                    print(totalsiniva[j])
                    print(totalconiva[j])  
    else: #si no es mayor a uno la cantidad de articulos se realiza lo siguiente 
        for i in range(N):# se realiza un for para imprimir en orden el articulo comprado
            print(listcodigo[i])
            print(listnombrearticulo[i])
            print(totalsiniva[i])
            print(totalconiva[i]) 
        
    return listcodigo, listnombrearticulo,totalsiniva,totalconiva,N #por ultimo se retorna los valores a mostrar
N=int(input("ingrese cantidad de productos diferentes a comprar"))
ivatotal=0 #se inicializan en cero los contadores q tomamos como variables 
totalfinal=0
listcodigo=[]# se crean las listas a llenar 
listnombrearticulo=[]
listcant=[]
listipoiva=[]
totalsiniva=[]
totalconiva=[]
iva=[]
articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}#se agrega en diccionarios los articulos
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}#se agrega en diccionario precio de cada articulo se define ppor los numeros de cada articulo
for i in range(N):#se realiza un ciclo for que va hasta n cantidad de articulos a comprar 
    listcodigo.append(int(input("codigo de articulo ")))# llenamos las listas con los datos que va ingresando a la lista 
    listcant.append(float(input("cantidad de articulos a comprar ")))
    listipoiva.append(int(input("tipo de iva ")))
    listnombrearticulo.append(articulos.get(listcodigo[i]))# se llena la lista en orden en posisicion i
    totalsiniva.append(listcant[i]*precios.get(listcodigo[i]))#se realiza las operaciones para sacar el subtototal de cada articulo donde se multiplica cant por valor del articulo guadado en diccionario
    if listipoiva[i]== 1:#se realizan un acondicion para definir el tipo de iva del articulo,donde si es 1 no aplica iva,y asi sucesivamente
        iva.append(0)
    elif listipoiva[i]==2:
        iva.append(totalsiniva[i]*0.05)
    elif listipoiva[i] ==3:
        iva.append(totalsiniva[i]*0.19)
    totalconiva.append(iva[i]+totalsiniva[i])#se agrega a la lista resultado de operacion para saber el total de iva por articulo
    totalfinal=totalfinal+totalconiva[i]#se realia suma de las listas para sacar el valor total con iva incluido de todos los articulos ingresados
    ivatotal=ivatotal+iva[i]# se suma todos los ivas aplicados para total de solo iva de toso los articulos
    #se imprime en orden de entrada los articulos codigo de articulo,nombre de articulo,el subtotal y el total con iva 
ordenar(listcodigo, listnombrearticulo,totalsiniva,totalconiva,N)    
print(totalfinal)
print(ivatotal)