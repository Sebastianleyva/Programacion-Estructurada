"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("cls")

paises=["Mexico","Brasil","España","Canada"]
pais1={"nombre":"Mexico",
       "Capital":"CDMX",
       "idioma":"Español",
       "pob":132000000
       }
pais2={"nombre":"Brasil",
       "Capital":"Rio de Janeiro",
       "idioma":"Portugues",
       "pob":150000000
       }
pais3={"nombre":"Canada",
       "Capital":"Otawua",
       "idioma":["Español","Frances"],
       "pob":13000000
       }
for i in pais1:
    print(f"{i}: {pais1[i]}")

#Agregar atributo
pais1["altitud"]=3000
for i in pais1:
    print(f"{i}: {pais1[i]}")
#Modificar atributo
pais1.update({"altitud":"2500"})
for i in pais1:
    print(f"{i}: {pais1[i]}")
#Quitar el ultimo atributo
pais1.popitem()

#Quitar elemento especifico
pais1.pop("Capital")