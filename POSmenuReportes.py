import os
import POSreportes_VtaxDia
import POSreportes_VtaxProd

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
        print ("0. SALIR")
        print ("----------------------------------")
        opcion = (input("Ingresar Opcion: "))
        if (opcion == "0"):
            return
        if (opcion == "1"):
            POSreportes_VtaxDia.BPF()            
        if (opcion == "2"):
            POSreportes_VtaxProd.reporta_vta_prod()            
       