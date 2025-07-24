"List (Array)"
"son colecciones o conjunto de datos/valores bajo un mismo nombre para acceder a los valores se hace con un indice numerico"
"nota: sus valores si son modificables"
"la lista es una coleccion ordenada y modificable. permite miembros duplicados"
import os
os.system("cls")
#Funciones más comunes de una lista
paises=["mexico","España","Brasil","Canada"]
numeros=[23,45,8,24]
varios=["hola",3.1415,33,True]
print(paises)
print(numeros)
print(varios)
#Recorrer la lista
#1
for i in paises:
    print(i)
#2
for i in range(0,len(paises)):
    print(paises[i])
#ordenar elemntos de una lista
paises.sort()
print(paises)
numeros.sort()
print(numeros)
#darle la vuelta al orden de la lista
paises.reverse()
print(paises)
#Add an element 
paises.append("Londres")
print(paises)
paises.insert(0,"Londres")
print(paises)
#delete a list's element
paises.pop(5)
print(paises)
paises.remove("Londres")
print(paises)
#Look for a list's element
respo="Brasil" in paises
print(respo)
#number of appearnes
print(numeros)
how=numeros.count(23)
print(how)
#Look for a value's position
print(paises)
posi=paises.index("mexico")
print(posi)
#put a list into another
print(numeros)
num2=[100,200]
print(num2)
numeros.extend(num2)
numeros.reverse()
print(numeros) 