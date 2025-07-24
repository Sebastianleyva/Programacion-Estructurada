peliculas=[]

def borrarpantalla():
    import os
    os.system("cls")
def esperartecla():
    opa=input("Oprima cualquier tecla para continuar :) ")
def agregarpeliculas():
    borrarpantalla()
    print("Agregar peliculas")
    peliculas.append(input("Ingrese la pelicula: ").upper().strip())
    print("La operaciones se realizó con exito")
def mostrarpeliculas():
    for i in range(0,len(peliculas)):
        print(f"{i+1}.-{peliculas[i]}")
    #print(peliculas)
def limpiarpelicula():
    borrarpantalla()
    resp=input("Va a borrar todas las peliculas\n¿Está seguro? si/no").lower().strip()
    if resp=="si":
        peliculas.clear()
        print("La operaciones se realizó con exito")
def buscarpelicula():
    buscar=input("Ingrese el nombre de la pelicula que desea buscar ").upper().strip()
    if buscar in peliculas():
        numero=0
        for i in range(0,len(peliculas)):
            if buscar==peliculas[i]:
                print(f"\nLa pelicula {buscar} está en la posición: {i+1}")
                numero+=1
        print(f"La pelicula {buscar} se encontró {numero} veces")
        print("La operaciones se realizó con exito")

    else:
        print("La pelicula no está en la lista")
def modificarpelicula():
    buscar=input("Ingrese el nombre de la pelicula que desea modificar ").upper().strip()
    for i in range(0,len(peliculas)):
        if buscar==peliculas[i]:
            resp=input("¿Desea actualizar la pelicula?").lower().strip()
            numero=0
            if resp=="si":
                peliculas[i]=input("Introduce el nuevo nombre de la pelicula").upper().strip()
                numero+=1
        print("La operaciones se realizó con exito")
    else:
        print("La pelicula no está en la lista")
def borrarpelicula():
    print("\tBorrar peliculas")
    borra=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
    if borra in peliculas:
        pre=input("¿Desea quitar o borrar la pelicula del sistema (Si/No) ").lower
        if pre=="si":
            for i in range(0,len(peliculas)):
                if borra==peliculas[i]:
                    print(f"La pelicula que se borro fue {peliculas[i]} y estaba en la casilla {i+1}")
                    peliculas.pop[i]
                    print("La operacion se realizo con éxito")

    else:
        print("Esa pelicula no existe en la lista")
    