"""
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("cls")

paises={"México","Brasil","España","canada"}
varios={True,"UTD",33,3,44}
print(varios)

#operaciones

paises.add("Mexico")

#paises.pop(2)

paises.remove("Mexico")

#ejemplo crear un programa que solicite los email de los alumnos de la 
#utd almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados
os.system("cls")
email=[]
de="si"
while de=="si":
    email.append(input("Escriba el email que desea agregar: "))
    de=input("¿Desea agregar otro email? si/no \n").lower()
email_set=set(email)
emails=list(email_set)

print(emails)

