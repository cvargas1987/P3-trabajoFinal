import os
import sys
import POSingresar
import datetime


class POS (object):
    
    def __init__(self, loginDefault,passDefault):
        self.loginDefault = loginDefault
        self.passDefault = passDefault
        x = datetime.datetime.now()
        self.fecha_actual = fecha_actual = ("%s/%s/%s" % (x.day, x.month, x.year))
 
    def calcularDescto (self, precio, porcDescto):
        return  round(((porcDescto * 0.01) * precio),2)
        
    
    def calcularImpuesto (self, precio, impuesto):
        return round(((impuesto * 0.01) * precio),2)
        
    
    def calcularCantidad (self,precio,cantidad):
        return round((precio * cantidad),2)


    def validarProducto (self, codigoValidar):
        try:
                f = open('productos.txt','r')
        except FileNotFoundError:
            print ("<<< ERROR!! No Existe Archivo de productos.txt >>>")  
            return (False) 

        for linea in f.readlines():
            try:    
                linea = linea.split(',') 
                codigo = linea[0]
                descripcion = linea[1]
                precio = linea [2]
                impuesto = linea [3]
                unidad = linea [4]
            except IndexError:
                print ("ERROR: verificar interfaz de productos")
                return False
            
            if (codigoValidar == codigo):
                datosP = (codigo, descripcion,precio,impuesto,unidad)
                return (datosP)

        return (False) 
    
    def validarFormaPago (self, ascii):
        try:
                f = open('pagos.txt','r')
        except FileNotFoundError:
            print ("<<< ERROR!! No Existe Archivo de pagos.txt >>>")  
            return (False) 

        for linea in f.readlines():
            linea = linea.split(',')
            try:    
               if ( ascii in linea[2] ):
                    return (linea[0],linea[1])
            except IndexError:
                msnError = ("ERROR: verificar interfaz de pagos")
                
        return (False) 

    def Totalizar (self, totalCuenta):
        
        saldoTemp = 0
        pagoTemp = 0
        pagadoTemp = 0
        saldoTemp = totalCuenta
        v = POSingresar.validar(self.loginDefault,self.passDefault)
        lineaPagoLista = []
        
        while True:   
            pos = POS(self.loginDefault,self.passDefault)
            os.system('cls')
            print ("----------------------------------")
            print ("    Sistema de Punto de Ventas    ")
            print ("               POS")
            print ("Fecha =  " + self.fecha_actual )
            print ("CJ    :" + v.validarLogin())
            print ("TOTAL : " + str(totalCuenta))
            print ("SALDO : " + str(saldoTemp))       
            print ("----------------------------------")
            print ("")
            try:
                f = open('pagos.txt','r')
                for linea in f.readlines():
                    linea = linea.split(',')
                    try: 
                        print ( "* Tecla <" + linea[2].strip() + "> : " + linea[1])
                    except IndexError as e:
                        msnError = (e)


            except FileNotFoundError:
                print ("--> ERROR!! No Existe Archivo pagos.txt")  

            print ("----------------------------------")
            pagoAscii = (input("Ingrese Forma de Pago: "))
            if (pagoAscii == "x" or pagoAscii == "X"):
                return False
            if (pos.validarFormaPago(pagoAscii) == False):
                msn = (input("<<< Pago Desconocido, vuelva a intentar >>>"))
            else:
                pagoId = pos.validarFormaPago(pagoAscii)[0]
                pagoDescrip = pos.validarFormaPago(pagoAscii)[1]
                print ("")
                print (pagoDescrip)
                while True:             
                    try: 
                        pagoMonto = float(input (" * Ingresar Monto a Pagar: "))
                        if (pagoMonto > 0):
                            pagadoTemp = round((pagoTemp + pagoMonto),2)
                            saldoTemp = round((saldoTemp - pagoMonto),2)
                            linea = (
                                "3" 
                                + "," 
                                + self.loginDefault 
                                + "," 
                                + "folio" 
                                + "," 
                                + pagoId 
                                + ","  
                                + str(pagoMonto) 
                                + "," 
                                + self.fecha_actual
                                + "," 
                                + "\n")

                            lineaPagoLista.append(linea)
                            if (saldoTemp <= 0):
                                os.system('cls')
                                print ("----------------------------------")
                                print ("    Sistema de Punto de Ventas    ")
                                print ("               POS")
                                print ("Cajero:")
                                print ("TOTAL : " + str(totalCuenta))
                                print ("CAMBIO : " + str(saldoTemp))       
                                print ("----------------------------------")
                                print ("")
                                return lineaPagoLista
                            else:
                                break
                        else:
                            msn = (input("<<< Monto a pagar debe ser mayor a Cero (0), vuelva a intentar >>>"))    
                    except ValueError: 
                        msn = (input("<<< Valor Invalido >>>"))
   
    def inicio(self):
        total = 0
        subtotal = 0
        totalImpuesto = 0 
        descuento = 0
        totalDescto = 0
        mostrar_lineaProducto = ""
        v = POSingresar.validar(self.loginDefault,self.passDefault)
        lineaDetalle = []
        montoDescto = 0
        
        while True:
            os.system('cls')
            print ("----------------------------------")
            print ("    Sistema de Punto de Ventas    ")
            print ("               POS")
            print ("Fecha =  " + self.fecha_actual )
            print ("CJ      : " + v.validarLogin())
            print ("TOTAL   : " + str(total))
            print ("SUBTOTAL: " + str(subtotal))
            print ("IMPUESTO: " + str(totalImpuesto))
            print ("DESCTO  : " + str(totalDescto))
            print ("----------------------------------")
            print ("d : Otorgar Descuento por Linea")
            print ("* : Totalizar")
            print ("x : Salir")
            print ("----------------------------------")
            while True: 
                if (descuento > 0):
                    print ("Descuento Otorgado por el " +  str(descuento) + "%")

                print (mostrar_lineaProducto)
                print ("----------------------------------")
                codigoTemp = (input("Ingresar codigo de Producto: "))
                print (" ")
                pos = POS(self.loginDefault, self.passDefault)

                if (codigoTemp == "*" and total > 0):
                    lineaPagos = pos.Totalizar(total)
                    if (lineaPagos == False):
                        return
                    else:
                        f = open ('ventas.txt','a')

                        f.write(
                        "1" 
                        + "," 
                        + self.loginDefault 
                        + "," 
                        + "folio" 
                        + "," 
                        + str(total) 
                        + "," 
                        + str(totalDescto)
                        + "," 
                        + "V" 
                        + "," 
                        + self.fecha_actual
                        + "," 
                        + "\n")
                        
                        for i in lineaPagos:
                            f.write (i)
                        for i in lineaDetalle:
                            f.write(i)
                        
                        f.close()
                        msn = (input("Cuenta Terminada Exitosamente, vuelva pronto !!"))
                        return

                if (codigoTemp == "x" or codigoTemp == "X"):
                    return

                if (codigoTemp == "d" or codigoTemp == "D"):
                    try:
                        descuento = int(input (" * Ingrese Porcentaje de Descuento: "))
                        break
                    except ValueError:
                        msn = (input("<<<Valor Invalido>>>"))
                        break
            
                if (pos.validarProducto(codigoTemp) == False):
                    msn = (input("<<<  No Existe Producto  <ENTER>>>>"))
                    break

                linea = (pos.validarProducto(codigoTemp))
                codigo = linea[0]
                descripcion = linea[1]
                precio = float(linea [2])
                impuesto = float(linea [3])
                unidad = linea [4]
                cantidad = float(1)
                
                

                if (unidad == "LT"):
                    try:
                        cantidad = float(input(" * Ingresar Cantidad de Litros: "))
                    except ValueError:
                        msn = (input("<<<Valor Invalido>>>"))
                        break

                    if (cantidad <= 0):
                        msn = (input("<<<Valor debe ser mayor a cero (0)>>>"))
                        break

                montoNeto = (pos.calcularCantidad(precio, cantidad))
                
                if (descuento > 0):
                    montoDescto = (pos.calcularDescto(montoNeto,descuento))
                    montoNeto = (montoNeto - montoDescto)
                    totalDescto = (totalDescto + montoDescto)
                    descuento = 0

                mostrar_lineaProducto = (descripcion + " x " + str(cantidad) + " = " + str(montoNeto))

                montoImpuesto = pos.calcularImpuesto(montoNeto,impuesto)    
                subtotal = round((subtotal + montoNeto),2)
                total = round((total + pos.calcularImpuesto(montoNeto, impuesto) + montoNeto),2)
                totalImpuesto = round((totalImpuesto + montoImpuesto),2)
                linea = (
                  "2" 
                + "," 
                + self.loginDefault 
                + "," 
                +"folio" 
                + "," 
                + codigoTemp 
                + "," 
                + str(montoNeto) 
                + "," 
                + str(montoImpuesto) 
                + "," 
                + str(montoDescto) 
                + "," 
                + descripcion 
                + ","
                + self.fecha_actual
                + "," 
                + "\n")
                
                lineaDetalle.append(linea)
                break