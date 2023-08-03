"""hacer un conversor de moneda,que lea un valor de pesos colombianos
y una tasa de cambio y laconvierta a un valor en dolares y lo
muestre en pantalla con 2 numeros decimales """

cantpesos=float(input("ingrese por favor la cantidad a cambiar a pesos: "))
tasacambio=float(input("ingrese por favor la tasa de cambio: "))
cantdolares=cantpesos/tasacambio
#print("lacantidad en dolare es :",cantdolares)
print(f"la cantidad en dolares es : USD$ {cantdolares:0,.2f}")