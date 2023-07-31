codg=int(input()) #pide codigo de tp entero 
np=input() #se pide nombre del producto tp string solo letra
cantp=float(input())#se pide cantidad de producto de tipo flotante
vu=float(input())#se pide valor unitario  de tipo flotante
tsiniva=cantp*vu #se hace operacion para saber el valor subtotal comprado 
tconiva=(((vu*0.19)+(vu))*cantp) #operacion para saber el total con iva incluido
#se realizan las impresiones a mostrar al usuario codido,producto,sutotal y total de la factura
print(codg)
print(np)
print(tsiniva)
print(tconiva)