N=int(input("ingrese la cantidad de los usuarios "))
for i in range(N):
    codigo=input("ingrese el codigo ")
    nombre=input("ingrese el nombre ")
    estado=input("estado V para vigente y S para suspendido ")
    estrato=int(input("ingrese el estrato "))
    consumo=float(input("ingrese el consumo mensual en cm cubico "))
    if estado=="v":
        if estrato==1:
            tbasica=10000
        elif estrato ==2:
            tbasica=20000
        elif estrato ==3:
            tbasica=30000
        elif estrato ==4:
            tbasica=45000
        elif estrato ==5:
            tbasica=60000
        elif estrato ==6:
            tbasica=70000
        else:
            print("ERROR DE ESTRATO ")
        valorconsumo=consumo*200
        vpagar=valorconsumo+tbasica
        print(f"\tel usuario {nombre}\n*El valor del consumo es: {valorconsumo:0,}\n*la tarifa basica: {tbasica:0,}\n*Debe pagar: {vpagar:0,}")



