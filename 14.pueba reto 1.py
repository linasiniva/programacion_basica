N=int(input())
ivatotal=0
totalfinal=0
for i in range(N):
    codigo=int(input())
    nombreProducto=input()
    cantidadProducto=float(input())
    ValorUnitario=float(input())
    tipoiva=int(input())
    totalsiniva=cantidadProducto*ValorUnitario
    if tipoiva== 1:
        iva=0
    elif tipoiva==2:
        iva=ValorUnitario*0.05
    elif tipoiva ==3:
        iva=ValorUnitario*0.19 
    total=iva*cantidadProducto
    totalconiva=(((iva)+(ValorUnitario))*(cantidadProducto))
    totalfinal=totalfinal+totalconiva
    ivatotal=ivatotal+total
    print(codigo)
    print(nombreProducto)
    print(totalsiniva)
    print(totalconiva)
if ivatotal==0.0:
    ivatotal=0
print(totalfinal)
print(ivatotal)

        

        
    
