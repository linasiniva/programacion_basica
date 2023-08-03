#/////////crear conjuntos /////////////
#grupo_a={"luis","lina"}
#grupo_a=set(["pedro","luis"])#lista con parametros
#metodo para agregar en un conjunto 
#conjunto={}
#estudiantes={"ana","juan","ana","juan","pedro","Ana"}

#estudiantes.add("ana")#agrega elemento
#estudiantes.discard("ana")#remover un elemnto 
#estudiantes.remove("juan")#para eliminar
#estudiantes.clear(grupo_a)#elima todo lo q tiene la lista

#elimna elemento alazar de un conjunto .pop
"""conjun=set(["ana","juan","ana","juan","pedro","Ana"])
print(conjun.pop())#elimina un elemento aleatorio de un conjunto 
print(conjun)"""

#elimina todos los elementos de un conjunto
"""conjun=set(["ana","juan","ana","juan","pedro","Ana"])
while conjun:
    print(conjun.pop())#elimina un elemento aleatorio de un conjunto 
print(conjun)"""

# set metodo metodo len()
"""conjun=set(["ana","juan","ana","juan","pedro","Ana"])
print(len(conjun))#me muestra la cantidad olongitud de la lista los elementos iguales los cuenta como el mismo"""

#SET (OPERACIONES PRINCIPALES)union,interseccion,diferencia,diferencia simetrica

#UNION
"""conjun_a={1,2,3}
conjun_b={"a","b","c"}

print(conjun_a|conjun_b)#imprime la union de los 2 conjuntos
print(conjun_a.union(conjun_b))#imprime la union de los 2 conjuntos"""

#INTERSECCION
"""a={1,2,3,"a"}
b={"a","b","c",2}

print(a&b)#imprime la interseccion de los 2 conjuntos {'a', 2}
print(a.intersection(b))#imprime la interseccion de los 2 conjuntos {'a', 2}
"""
#DIFERENCIA-
"""c={1,2,3,"a"}
d={"a","b","c",2}

print(c-d)#imprime la diferencia de los conjuntos
print(c.difference(d))"""

#DIFERENCIA SIMETRICA
"""f={1,2,3,"a"}
e={"a","b","c",2}

print(f-e)#imprime la diferencia simetrica de los conjuntos
print(f.symmetric_difference(e))"""

#operaciones con conjuntos
"""
a={1,2,3,"a"}
b={"a","b","c",2}
c={"hola",25}
print(a,b)#muestra los2 conjuntos {1, 2, 3, 'a'} {'c', 'a', 2, 'b'}
print(a or b)#muestra {1, 2, 3, 'a'}
print(a and b)#muestra cualquiera de los 2 conjunto {'c', 'a', 2, 'b'}
print(a==c)#compara si un conjunto es igual alotro en este caso es False
"""
#//////////////////
"""estudiantes={"ana","juan","ana","juan","pedro","Ana","pedro","pedro","fani"}
estd=set(["ana","juan","ana","juan","pedro"])
print(estudiantes.issubset(estd))#si elconjunto esta dentro del otro 
print(estudiantes.issuperset(estd))#se dice q estidiantes es un superconjunto de estd (True)
"""
#copia de conjunto en otro conjunto 
"""
conj=set(["lina","barbara","alex","eider"])
copia=conj.copy()
print(conj)
print(copia)
"""
#////////////ejercicio////////////
A={"z",8,"9",(10,20,30),8,9,8}
B={7,8,9,}
C={1,2,3}

print(len(A))#Cuántos elementos tiene el conjunto A? = 5
print(B.union(C))#Agregar al conjunto B, los números 1,2,3 ={1, 2, 3, 7, 8, 9}
print(B in A)#¿B está en A? =False
print(B == A)#¿B es igual a A? =False

