def borrar():
        import os
        os.system("cls")

def esperartecla():
    opa=input("Oprima cualquier tecla para continuar :)")

def menu():
    borrar()
    print("\t\U0001F4DD..::Sistema de Gestión de Contactos::..\U0001F4DD\n")
    print(" 1.-Agregar contacto\n 2.-Mostrar todos los contactos\n 3.-Buscar contacto por nombre\n 4.-Modificar contacto\n 5.-Borrar contacto\n 6.-SALIR\n")
    opcion=input("\U0001F449 Elige una opción (1-6): ").strip()
    return opcion
    
def agregarconta(agenda):
    borrar()
    print("\t...Agregar contacto...")
    nombre=input("Nombre: ").upper().strip()
    if nombre in agenda:
        print("Ese contacto ya existe")
    else:
        tel=input("Télefono: ").upper().strip()
        correo=input("Email: ").lower().strip()
        agenda[nombre]=[tel,correo]
        print("La acción se realizó con éxito")
        
def mostrarconta(agenda):
    borrar()
    print("\t Mostrar contactos")
    if not agenda:
        print("No hay contactos en la agenda")
    else:
        print(f"{'nombre':<15} {'Telefono':<15} {'Correo'}")
        for nombre,fila in agenda.items():
            print(f"{nombre:<15} {fila[0]:<15} {fila[1]}")

def buscarconta(agenda):
    borrar()
    print("\t..::Buscar Contactos::..")
    if not agenda:
        nombre=input("Ingrese el nombre del contacto que desea ingresar: ").upper().strip()         
        if nombre in agenda:
            print(f"{'nombre':<15} {'Telefono':<15} {'Correo'}")
            print(f"-"*60)
            print(f"{'nombre':<15} {agenda[nombre][0]:<15} {agenda[nombre][1]}")
            print(f"-"*60)
        else:
            print("Ese contacto no existe")
    else:
        print("No hay contactos en la agenda")

def modificarcont(agenda):
    borrar()
    print("\t..::Modificar Contactos::..")
    if not agenda:
        nombre=input("Ingrese el nombre del contacto que desea modificar: ").upper().strip()         
        if nombre in agenda:
            print("Valores actuales")
            print(f"Nombre: {nombre:<15}\n Télefono: {agenda[nombre][0]:<15}\n E-mail: {agenda[nombre][1]}")
            pregun=input("¿Desea cambiar algun valor?").lower().strip()
            if pregun=="si":
                tel=input("Télefono: ").strip()
                correo=input("Email: ").lower().strip()
                agenda[nombre]=[tel,correo]
                print("La acción se realizó con éxito")
        else:
            print("Ese contacto no existe")
    else:
        print("No hay contactos en la agenda")

def borrarcont(agenda):
    borrar()
    print("\t..::Borrar Contactos::..")
    if not agenda:
        nombre=input("Ingrese el nombre del contacto que desea borrar: ").upper().strip()         
        if nombre in agenda:
            print(f"Nombre: {nombre:<15}\n Télefono: {agenda[nombre][0]:<15}\n E-mail: {agenda[nombre][1]}")
            pregun=input("¿Desea eliminar este contacto?").lower().strip()
            if pregun=="si":
                agenda.pop(nombre)
                print("La acción se realizó con éxito")
        else:
            print("Ese contacto no existe")
    else:
        print("No hay contactos en la agenda")
