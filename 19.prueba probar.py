n = int(input())
listacodigo = []
listanombre = []
listacantidad = []
listavalor_unitario = []
listatipo_de_iva = []
valor_iva=[]
valor_producto=[]
valor_unitario_final=[]
valor_total_producto=[]
valor_totaliva_producto=[]
total_compra =0
total_iva = 0
                                                           
for i in range(n): 
    
    listacodigo. append(int(input()))
    listanombre.append(input())
    listacantidad.append(float(input()))
    listavalor_unitario.append (float(input()))
    listatipo_de_iva.append (int(input()))
    
    if listatipo_de_iva[i]==1:
         valor_iva.append(0)
    elif listatipo_de_iva[i]== 2:
         valor_iva.append(0.05)
    elif listatipo_de_iva[i]== 3:
         valor_iva.append (0.19)
         
    valor_unitario_final.append (listavalor_unitario[i]*(1+valor_iva[i]))                                                    
    valor_producto.append(listacantidad[i]*listavalor_unitario[i])  
    valor_totaliva_producto.append (listavalor_unitario[i]*valor_iva[i]*listacantidad[i]) 
    valor_total_producto.append (valor_unitario_final[i]*listacantidad[i])   
    
    total_compra=total_compra+valor_total_producto[i]
    total_iva= total_iva +valor_totaliva_producto[i]
     
       
    
print (len(listacodigo))    
print (len(listanombre))   
print(len(listacantidad))    
print (len(listavalor_unitario)) 
print (len(listatipo_de_iva))
    
for i in range(n):
       
    print(listacodigo [i])
    print(listanombre[i])
    print(valor_producto[i])
    print(valor_total_producto[i])

print(total_compra)
print (total_iva)