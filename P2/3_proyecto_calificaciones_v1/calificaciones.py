


def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    opa=input("\t\U0001F552..::Oprima cualquier tecla para continuar::..\U0001F552 ")

def menu_principal():
    print("\t\U0001F4C2...:::Sistema de Gestión de Calificaciones:::...\U0001F4C2\n")
    opci=input("Seleccione una opción \n 1.-Agregar\n 2.-Mostrar\n 3.-Calcular promedio\n 4.-Salir\n\U0001F449 ")
    return opci

def agregarcali(lista):

    borrarpantalla()
    print("\t\U0001F4DD..::Agregar Calificaciones::..\U0001F4DD")
    nombre=input("\U0001F464 Escriba el nombre del alumno: \n").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                #calificaciones.append(float(input(f"Escriba la calificación {i}: ")))
                cal=float(input(f"\U0001F4DD Escriba la calificación {i}: "))
                if cal>=0 and cal<=10:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("\t\u274C..::Ingrese un valor dentro del rango del 1 al 10::..\u274C")
            except ValueError:
                print("\u274C Escriba solo valores numericos")
    lista.append((nombre,calificaciones))
    print("\t\u2705Operación realizada con éxito\u2705")

def mostrarcali(lista):
    borrarpantalla()
    print("\tMostrar calificaciones\n")
    if len(lista)>0:
        print(f"{'Nombre':<15}  {'Cal1':<10}  {'Cal2':<10}  {'Cal3':<10}")
        for i in(lista):
            print(f"{i[0]:<15}  {i[1]:<10}  {i[2]:<10}  {i[3]:<10}")
        cuantos=len(lista)
        print(f"Son {cuantos} alumnos")
    else:
        print("\t\u274CNo hay calificaciones en el sistema\u274C")

def calcularprome(lista):
    borrarpantalla()
    print("\t\U0001F9EE..::Calcular Promedios::..\U0001F9EE\n")
    if len(lista)>0:
        print(f"{'Nombre':<15}  {'Promedio':<10} ")
        promgrup=0
        for i in lista:
            nombre=i[0]
            promedio=(i[1]+i[2]+i[3])/3
            promgrup+=promedio
        print(f"{nombre:<15}  {promedio:.2f} ")
        print(f"El promedio grupal es: {promgrup}")
    else:
        print("\t\u274C..::No hay calificaciones en el sistema::..\u274C")
