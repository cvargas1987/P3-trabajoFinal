import os

def reporta_vta_prod():
    
    while True:
        total = 0
        os.system('cls')
        print ("----------------------------------")
        print ("    Sistema de Punto de Ventas    ")
        print ( "REPORTE DE VENTAS POR PRODUCTO")
        print ("----------------------------------")
        print ( " ")
        while True: 
            producto = (input("Ingresa el codigo del producto: "))
            try:
                f = open('ventas.txt','r')
            except FileExistsError:
                msn = (input("ERROR: no existe el archivo de ventas")) 
                break
            
            if (producto == '0'):
                return

            for linea in f.readlines():
                linea = linea.split(',')
                if (linea[0] == '2' and linea[3] == producto):
                    total = float(linea[4]) + total
            break
        msn =  (input("Total en ventas: " + str(total) + "$"))
        


        