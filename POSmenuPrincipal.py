import POSmenuAdministrativo
import POSmenuReportes
import os

def menuPrincipal():
    while True:
        os.system('cls')
        print ("----------------------------------")
        print ("    Sistema de Punto de Ventas    ")
        print ( "        MENU PRINCIPAL")
        print ("----------------------------------")
        print ( " ")
        print ("1. Sistema POS")
        print ("2. Reportes")
        print ("3. Menu Administrativo")
        print ("0. SALIR")
        print ("----------------------------------")
        opcion = (input("Ingresar Opcion: "))
        if (opcion == "0"):
            break
        #if (opcion == "1"):
            
        if (opcion == "2"):
            POSmenuReportes.menuReportes()
        if (opcion == "3"):
            POSmenuAdministrativo.menuAdministrativo()
