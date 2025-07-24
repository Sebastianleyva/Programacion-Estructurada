import agenda

def main():
    agenda_con={}
    rep=True
    while rep:
        agenda.borrar()
        opcion=agenda.menu()

        if opcion=="1":
            agenda.agregarconta(agenda_con)
            agenda.esperartecla()
        elif opcion=="2":
            agenda.mostrarconta(agenda_con)
            agenda.esperartecla()
        elif opcion=="3":
            agenda.buscarconta(agenda_con)
            agenda.esperartecla()
        elif opcion=="4":
            agenda.modificarcont(agenda_con)
            agenda.esperartecla()
        elif opcion=="5":
            agenda.borrarcont(agenda_con)
            agenda.esperartecla()
        elif opcion=="6":
            agenda.borrar()
            print("Terminó el programa...")
            opcion=False
        else:
            opcion=True
            print("Opción no valida, intente de nuevo")

main()