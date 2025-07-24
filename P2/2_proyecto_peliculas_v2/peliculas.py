#Crear un objeto que permita almacenar los siguientes atributos; nombre, categpria, clasificación, genero, idioma
#pelicula={"nombre":"","categoria":"","clasificacion":"","genero":"","idioma":""}
pelicula={}

def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    opa=input("Oprima cualquier tecla para continuar :) ")

def crearpeliculas():
    borrarpantalla()
    print("\t..Agregar Peliculas..")
    #atributo=input("Ingresa la caracterisica")
    #valor_a=input("Ingresa el valor de la caracterisica")
    pelicula.update({"nombre":input("Ingrese el nombre de la pelicula: \n").upper().strip()})
    pelicula.update({"categoria":input("Ingrese la categoria de la pelicula: \n").upper().strip()})
    pelicula.update({"nombre":input("Ingrese la clasificación de la pelicula: \n").upper().strip()})
    pelicula.update({"clasificación":input("Ingrese el genero de la pelicula: \n").upper().strip()})
    pelicula.update({"idioma":input("Ingrese el idioma de la pelicula: \n").upper().strip()})
    print("La operaciones se realizó con exito")

def mostrarpelicula():
    borrarpantalla()
    print("Mostrar Caracteristicas")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i}.-{pelicula[i]}")
    else:
        print("No hay ningún elemento en la lista")

def borrarpelicula():
    borrarpantalla()
    print("\t..Borrar Pelicula..")
    if len(pelicula)>0:
        conf=input("¿Está seguro de borrar las peliculas? si/no \n").lower().strip()
        if conf=="si":
            pelicula.clear()
            print("La operación se realizo con exito")
    else:
        print("El diccionario está vacio, no hay nada que borrar")

def agregarpeliculas():
    borrarpantalla()
    print("\t..Agregar Atributos..")
    carac=input("Escriba el nombre de la caracteristica que desea agregar: ").lower().strip()
    valor=input("Escriba el valor que va a tener la caracteristica que agregó: ").upper().strip()
    pelicula.update({carac:valor}).upper().strip()
    print("La operaciones se realizó con exito")

def modificarpelicula():
    borrarpantalla()
    print("Modificiar Caracteristicas")
    if len(pelicula)>0:
        for i in pelicula:
            resp=input(f"¿Desea cambiar el valor de {i}  si/no\n").lower().strip()
            if resp=="si":
                pelicula.update({f"{i}":input("Ingrese el nuevo valor: \n").upper().strip()})
                print("La operación se realizo con exito")
    else:
        print("Su lista está vacia")

def borraratributo():
    borrarpantalla()
    print("Borrar Caracteristica")
    if len(pelicula)>0:
        print("\t\tValores actuales")
        for i in pelicula:
            print(f"{i}.-{pelicula[i]}")
        pregu=input("¿Desea borrar alguna caracterisica? si/no\n").lower().strip()
        if pregu=="si":
            borra=input("Ingrese la caracteristica que desea borrar: ").lower().strip()
            for j in range(0,4):
                if borra==j:
                    pelicula.pop(j)
                else:
                    print("Esa caracteristica no esta en la lista")
    else:
        print("Su lista esta vacia")
