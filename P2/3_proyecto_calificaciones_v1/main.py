import calificaciones
def main():
    datos=[]
    opci=True
    while opci:
        calificaciones.borrarpantalla()
        opci=calificaciones.menu_principal()
    
        match opci:
            case "1":
                calificaciones.agregarcali(datos)
                calificaciones.esperartecla()
            case "2":
                calificaciones.mostrarcali(datos)
                calificaciones.esperartecla()
            case "3":
                calificaciones.calcularprome(datos)
                calificaciones.esperartecla()
            
            case "4":
                calificaciones.borrarpantalla()
                opci=False
                print("\t\U0001F389..::Ha terminado el programa::..\U0001F389")
            case "5":
                calificaciones.buscar()
                calificaciones.esperartecla()
            case _:
                print("Valor no valido, ingrese uno que lo sea")
                
main()