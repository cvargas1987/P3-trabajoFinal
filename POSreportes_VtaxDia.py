import os
def BPF():
    while True:
        total = 0
        os.system('cls')
        print("----------------------------------")
        print("    Sistema de Punto de Ventas    ")
        print("    REPORTE DE VENTAS POR FECHA")
        print("----------------------------------")
        print(" ")
        while True:
            fecha = (input("Ingresa la fecha (DD/MM/AAAA) de búsqueda: "))
            if (fecha == '0'): 
                return
            try:
                f = open('ventas.txt', 'r')
            except FileExistsError:
                msn = (input("ERROR: no existe el archivo de ventas"))
                break

            if (fecha == 0):
                return

            for linea in f.readlines():
                linea = linea.split(',')
                if (linea[0] == '1' and linea[6] == fecha):
                    total = float(linea[3]) + total
            break
        msn = (input("Total en ventas por fecha: " + str(total) + "$"))