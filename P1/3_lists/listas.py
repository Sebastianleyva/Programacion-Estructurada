"Ejemplo 1 crear una lista de numeros e imprimir el contenido"
import os
os.system("cls")
numeros=[1,2,3,4]
print(numeros)
"2- crear una lista de palabras y posteriormente buscar la coincidencia de una palabra"
palabras=["hola","adios","numero","pollo"]
#1
buscar_=input("Escriba la palabra a buscar: ")
if buscar_ in palabras:
    print("Si se encontró la palabra")
else:
    print("La palabra no está en la lista")
#2
encontro=False
cuantas=0
for i in palabras:
    if i==buscar_:
        encontro=True
        cuantas+=1
if encontro:
    print("Si se encontró la palabra")
else:
    print("La palabra no está en la lista")
 
os.system("cls")
"3- añadir elementos a la lista"
num=[]
respuesta=input("¿quiere agregar otro elemnto? si/no ").lower
while respuesta=="si":
    num.append(float(input("dame otro numero: ")))
    respuesta=input("¿quiere agregar otro elemnto? si/no ").lower

"4-crear una multidimensional que permita almacenar el nombre y telefono de una agenda"
