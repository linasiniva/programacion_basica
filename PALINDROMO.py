#Programa que reciba una palabra y nos indique si esta palabra es un palíndromo 
#(se escribe igual de izq a der y de der a izq)
'''Entradas: 
luz azul    
ana 
Isaac no ronca asi  
Lavan esa base naval 

Salidas:
Es palíndromo 
No es palíndromo '''

def limpiarCaracteres(palabras):
    palabras = palabras.lower()
    palabras = palabras.replace(" ","")
    palabras = palabras.replace("á","a")
    palabras = palabras.replace("é","e")
    palabras = palabras.replace("í","i")
    palabras = palabras.replace("ó","o")
    palabras = palabras.replace("ú","u")
    return palabras   

def palindromo(palabras):
    #comparar palabras 
    palabrainv=palabras[::-1]
    if palabras==palabrainv:
        return True
    else:
        return False

def palabras():
    #pide la palabra para compararla
    palabras=input("escriba una palabra, para saber si es palíndromo: ")
    palabras=limpiarCaracteres(palabras)
    es_palindromo=palindromo(palabras)
    if es_palindromo==True:
        print("es palíndromo")
    else:
        print("NO es palíndromo")

if __name__=='__main__':
    palabras()