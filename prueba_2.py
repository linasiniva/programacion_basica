# PRUEBA 2 
N=int(input())#se ingresa cantIdad de producto a procesar de tipo entero
#se inicializan variables en cero para utilizar como contadores
ivatotal=0 
totalfinal=0
for i in range(N):#se realiza un for que va hasta cantidad de producto ingresada
    #se pide los datos a igresar 
    codigo=int(input())
    nombreProducto=input()
    cantidadProducto=float(input())
    ValorUnitario=float(input())
    tipoiva=int(input())
    #se hace operacion para saber el valor del subtotal
    totalsiniva=cantidadProducto*ValorUnitario
    #se hace un condicional donde me da a elegir 3 opciones 
    if tipoiva== 1: #donde si es igual a "1" el iva es =0
        iva=0
    elif tipoiva==2:#donde si es igual a "2" el iva es igual al 5%
        iva=totalsiniva*0.05
    elif tipoiva ==3:#y si es igual a "3" el iva es igual al 19%
        iva=totalsiniva*0.19
        
    totalconiva=iva+totalsiniva #se realiza operacion para el total con iva incluido de todos los products
    totalfinal=totalfinal+totalconiva #se suman todos los productos comprados con iva incluido
    ivatotal=ivatotal+iva#se suman el total de iva que tienen los prodcutos comprados
    #se impreme los resultados A mostrar de la factura
    print(codigo)
    print(nombreProducto)
    print(totalsiniva)
    print(totalconiva)
print(totalfinal)
print(ivatotal)