import peliculas

opcion = True
while opcion:
    peliculas.borrarpantalla()
    print(f"\n\t\t.:: Gestión de películas ::. \n1.- Agregar \n2.- Borrar \n3.- Modificar \n4.- Mostrar \n5.- Buscar \n6.- Limpiar \n7.- Salir")
    seleccion = input("Elige una opción: ")

    match seleccion:
        case "1":
            peliculas.agregarpeliculas()
            peliculas.esperartecla()
        case "2":
            peliculas.borrarpelicula()
            peliculas.esperartecla()
        case "3":
            peliculas.modificarpelicula()
            peliculas.esperartecla()
        case "4":
            peliculas.mostrarpeliculas()
            peliculas.esperartecla()
        case "5":
            peliculas.buscarpelicula()
            peliculas.esperartecla()
        case "6":
            peliculas.limpiarpelicula()
            peliculas.esperartecla()
        case "7":
            opcion = False
            peliculas.borrarpantalla()
            print("Terminaste la ejecución del sistema\n .:: Gracias :) ::.")
        case _:
            print("Opción no válida, intenta de nuevo")
            peliculas.esperartecla()
