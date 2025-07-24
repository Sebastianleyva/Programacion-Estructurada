#Crear un objeto que permita almacenar los siguientes atributos; nombre, categpria, clasificación, genero, idioma
#pelicula={"nombre":"","categoria":"","clasificacion":"","genero":"","idioma":""}
import mysql.connector 

pelicula={}

def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    opa=input("Oprima cualquier tecla para continuar :) ")

def conectar():
    try:
        conexion=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="bd_peliuclas")
        return conexion
    except:
        print(f"El error es malo")
        return None

def crearpeliculas():
    borrarpantalla()
    print("\t..Agregar Peliculas..")
    conexiondb=conectar()
    if conexiondb!=None:
         #atributo=input("Ingresa la caracterisica")
        #valor_a=input("Ingresa el valor de la caracterisica")
        pelicula.update({"nombre":input("Ingrese el nombre de la pelicula: \n").upper().strip()})
        pelicula.update({"categoria":input("Ingrese la categoria de la pelicula: \n").upper().strip()})
        pelicula.update({"clasificacion":input("Ingrese la lasificacion de la pelicula: \n").upper().strip()})
        pelicula.update({"genero":input("Ingrese el genero de la pelicula: \n").upper().strip()})
        pelicula.update({"idioma":input("Ingrese el idioma de la pelicula: \n").upper().strip()})
        print("La operaciones se realizó con exito")

        crusor=conexiondb.cursor()
        sql="INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
        val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
        crusor.execute(sql,val)
        conexiondb.commit()
        print("\n\t\t..::LA OPERACIÓN SE REALIZÓ CON EXITO::..")

def mostrarpelicula():
    borrarpantalla()
    print("Mostrar Caracteristicas")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i}.-{pelicula[i]}")
    else:
        print("No hay ningún elemento en la lista")

