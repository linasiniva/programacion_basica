N=int(input())#se ingresa cant de products a procesar
ivatotal=0#se inicializan en cero para tomar variable como contadores 
totalfinal=0
#se almacena la informacion que se ingresa de los productos  en listas
listcodigo=[]
listnombre=[]
listcant=[]
listVunt=[]
listipoiva=[]
totalsiniva=[]
totalconiva=[]
iva=[]
for i in range(N):#se realiza un ciclo for que va hasta la cant de products
    #se pide los datos de entrada de cada product 
    listcodigo.append(int(input()))#por medio de append se añade cada codigo ingresado al conjunto de lista q hay
    listnombre.append(input())#igualmente se añade a la lista lo nombres ingresados de tipo string
    listcant.append(float(input()))
    listVunt.append(float(input()))
    listipoiva.append(int(input()))
    totalsiniva.append(listcant[i]*listVunt[i])#se realiza operacion de cada lista en su respectiva posicion para saber el subtotal de cada productos ingresados
    if listipoiva[i]== 1: #se realiza condicional  con 3 opciones de tipo de iva si seleciona 1 no se aplica iva
        iva.append(0)
    elif listipoiva[i]==2:#si el tipo de iva es igaul a 2 entonces es el iva del 5%
        iva.append(totalsiniva[i]*0.05)
    elif listipoiva[i] ==3:#en este caso seria tipo de iva del 19%
        iva.append(totalsiniva[i]*0.19)
    totalconiva.append(iva[i]+totalsiniva[i])#aqui se toma ya el rta del subtotal ya realizado y se le agrega el iva para el total con iva incluido 
    totalfinal=totalfinal+totalconiva[i]#se suma todos los totales de los productos de guardados en listas
    ivatotal=ivatotal+iva[i]#se suman todos los ivas para la suma de un total de solo iva de los productos
  
for i in range(N): #se realiza un for para la impresion de cada prdcuts ingresado en su orden
    print(listcodigo[i])
    print(listnombre[i])
    print(totalsiniva[i])
    print(totalconiva[i])      
print(totalfinal)
print(ivatotal)