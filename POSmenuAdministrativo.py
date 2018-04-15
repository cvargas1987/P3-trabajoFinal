import os
import POSAdministrarUsuario

def menuAdministrativo():
    while True:
        os.system('cls')
        print ("----------------------------------")
        print ("    Sistema de Punto de Ventas    ")
        print ( "      MENU ADMINISTRATIVO")
        print ("----------------------------------")
        print ( " ")
        print ("1. Creacion/Consulta de Usuarios")
        print ("2. Creacion/Consulta de Productos")
        print ("3. Creacion/Consulta de Formas de Pago")
        print ("4. Parametros de Empresa")
        print ("0. SALIR")
        print ("----------------------------------")

        opcion = (input("Ingresar Opcion: "))
        if (opcion == "0"):
            break
        if (opcion == "1"):
            m = POSAdministrarUsuario.usuariosAdministrar()
            m.ingresar()
            
        if (opcion == "2"):
            break
        if (opcion == "3"):
            break
        if (opcion == "4"):
            break