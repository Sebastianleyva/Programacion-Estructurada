"Crear un proyevto que permita gestionar peliculas. colocar un menu de opciones"
""
"Notas: "
"1-utlizar funciones y mandarlas a llamar desde otro modulo"
"2- utilizar dict para almacenar los atributos (nombre, categoria, clasificación)"

import backend as peliculas

opcion = True
while opcion:
    peliculas.borrarpantalla()
    print(f"\n\t\t.:: Gestión de películas ::. \n1.- Crear \n2.- Borrar \n3.- Mostrar \n4.- Buscar \n5.- Modificar \n6.- Salir \n")
    seleccion = input("Elige una opción: ")

    match seleccion:
        case "1":
            peliculas.crearpeliculas()
            peliculas.esperartecla()
        case "2":
            peliculas.borrarpelicula()
            peliculas.esperartecla()
        case "3":
            peliculas.mostrarpelicula()
            peliculas.esperartecla()
        case "4":
            peliculas.buscarpeliculas()
            peliculas.esperartecla()
        case "5":
            peliculas.modificarpelicula()
            peliculas.esperartecla()
        case "6":
            opcion = False
            peliculas.borrarpantalla()
            print("Terminaste la ejecución del sistema\n .:: Gracias :) ::.")
        case _:
            print("Opción no válida, intenta de nuevo")
            peliculas.esperartecla()
