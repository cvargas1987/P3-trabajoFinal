import os
import re 

class productosAdministrar (object):
    
    def validarPatron (self,campo):
        patron = '[a-z0-9][a-z0-9]'
        if re.match(patron,campo):
            return True
        else:
            msn = (input("Valor Invalido!"))
            return False
    
    def validarLogin (self, productValidar):
        try:
                f = open('productos.txt','r')
        except FileNotFoundError:
            print ("--> ERROR!! No Existe Archivo de Productos")  
            return (False) 

        for linea in f.readlines():

            linea = linea.split(',')
            pr_codigo = linea[0]
            

            if (productValidar == pr_codigo):
                return (True)
        return (False)
        
    def principal (self):
        while True: 
            os.system('cls')
            print ("----------------------------------")
            print ("    Sistema de Punto de Ventas    ")
            print ( "   CREAR/CONSULTAR PRODUCTOS")
            print ("----------------------------------")
            print ( " ")

            while True: 
                print ("Oprimir cero (0) para Salir") 
                pr_codigo = (input("Codigo de Producto: "))
                if (pr_codigo == "0"):
                    return

                v = productosAdministrar()
                if (v.validarPatron(pr_codigo) == True): 
                    if (v.validarLogin(pr_codigo) == True):
                        msn = (input("Este Producto ya Existe <ENTER>"))
                    else: 
                        break
                    
            pr_descrip = (input("Descripcion: "))
            while True:
                try:
                    pr_precio = float(input("Precio: " ))
                    break
                except ValueError: 
                    print ("Valor Invalido")
            while True:
                try:
                    pr_impuesto = float(input("Impuesto: %"))
                    break
                except ValueError:
                    print ("Valor Invalido")

            while True:
                pr_unidad = (input("Unidad (UND) o Litros (LT)")).upper()
                if (pr_unidad == "LT" or pr_unidad == "UND"):
                    break

            print (" ")
            opcion = (input("Datos Correctos ?"))
            if (opcion.lower() == "s"):
                    f = open ('productos.txt','a')
                    f.write(pr_codigo 
                    + "," 
                    + pr_descrip 
                    + "," 
                    + str(pr_precio) 
                    + "," 
                    + str(pr_impuesto) 
                    + "," 
                    + pr_unidad 
                    + ","
                    + "\n")

                    f.close()
                    opcion = (input("Datos Guardados Correctamente <ENTER>"))
        else: 
            x = input("Valor Invalido")