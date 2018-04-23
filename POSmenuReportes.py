import os
import POSreportes_VtaxDia

def menuReportes():
    while True:
        os.system('cls')
        print ("----------------------------------")
        print ("    Sistema de Punto de Ventas    ")
        print ( "         MENU REPORTES")
        print ("----------------------------------")
        print ( " ")
        print ("1. Reporte de Venta por rango de Fecha")
        print ("2. Reporte de Ventas por producto")
        print ("3. Reporte de Ventas por Forma de Pago")
        print ("4. Reporte de Ventas por Usuario")
        print ("0. SALIR")

        opcion = (input("Ingresar Opcion: "))
        if (opcion == "0"):
            return
        if (opcion == "1"):
            POSreportes_VtaxDia.BPF()            
        if (opcion == "2"):
            break
        if (opcion == "3"):
            break
        if (opcion == "4"):
            break