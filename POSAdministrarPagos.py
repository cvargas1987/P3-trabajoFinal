import os
import os.path

class IngresarPagos (object):
    
    def validarExisteDato (self, posicion, datoComparar):
        try:
            f = open('pagos.txt','r')
        except FileNotFoundError:
            print ("<<< ERROR!! No Existe Archivo de pagos.txt >>>")  
            return (True)
            

        for linea in f.readlines():
            linea = linea.split(",")
            try:
                if datoComparar in linea[posicion]:
                    return ("Ya Existe")
            except IndexError:
                return (True)
        return (True)

    def OpcionCrear(self):
        while True: 
            while  True:
                os.system('cls')
                print ("----------------------------------")
                print ("    Sistema de Punto de Ventas    ")
                print ("      MENU CREACION DE PAGOS   ")
                print ("----------------------------------")
                
                p = IngresarPagos()
                h = False
                
                id = input ("ID: <(0) Salir> " )
                if (id == "0"):
                    return

                validarD = p.validarExisteDato(0,id) 
                if  validarD is not True:
                    msn = (input(validarD))    
                    break

                forma = input("Descripcion: (Efectivo, Tarjerta de Credito, etc...): ")
                asc = input("Teclado: ")
                validarD = p.validarExisteDato(2,asc) 
                if  validarD is not True:
                    msn = (input(validarD))    
                    break
                while True:
                    msn = (input("Datos correctos ? S/N: "))
                    if (msn == "N" or msn == "n"):
                        return
                    elif (msn == "S" or msn == "s"):
                        break

                archivo = open('pagos.txt', 'a')
                archivo.write(id + "," + forma + "," + asc + "\n")
                archivo.close()
                msn = (input("<<< Datos agregados Correctamente, oprimir cualquier tecla para continuar. >>>"))

    def OpcionCambiar(self):
        import os.path
        com = os.path.isfile("pagos.txt")
        if com == False:
            print ("Ingrese los datos")
        else:
            with open("pagos.txt") as file:
                datos = ''
                iidd = input("Ingrese el ID de la transacciónn a cambiar: ")
                for linea in file:
                    id = linea[0]
                    if id in iidd:
                        forma = input("Ingrese la nueva forma de pago (efectivo, tarjerta o cupon): ")
                        asc = input("Ascii para totalizar la transacción: ")
                        cambio = (id + "," + forma + "," + asc + "," + "\n")
                        linea = cambio
                    datos += linea
                file.close()
            with open("pagos.txt", "w") as file: 
                file.write(datos)
                file.close()
    
    def menuPagos(self):
        os.system('cls')
        print ("----------------------------------")
        print ("    Sistema de Punto de Ventas    ")
        print ("      MENU CREACION DE PAGOS   ")
        print ("----------------------------------")
        print (" ")
        print ("1. Crear pago")
        print ("2. Modificar pago")
        print ("0. Salir")
        print (" ")
        print ("----------------------------------")

    def principal (self):
        while True:
            MenuOpciones = IngresarPagos()
            MenuOpciones.menuPagos()
            opc = input("Ingresar Opcion: ")
            if opc == "1":
                MenuOpciones.OpcionCrear()
            if  opc == "2":
                MenuOpciones.OpcionCambiar()
            if opc == "0":
                return

