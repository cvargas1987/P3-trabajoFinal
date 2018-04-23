import os
import sys
import POSingresar


class POS (object):
    
    def __init__(self, loginDefault,passDefault):
        self.loginDefault = loginDefault
        self.passDefault = passDefault
 
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
            try:    
                linea = linea.split(',') 
                pagoId = linea[0]
                pagoDescrip = linea[1]
                pagoAscii = linea [2] 
            except IndexError:
                print ("ERROR: verificar interfaz de pagos")
                return False
            
            if (ascii == pagoAscii):
                return (pagoId, pagoDescrip)

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
            print ("CJ    :" + v.validarLogin())
            print ("TOTAL : " + str(totalCuenta))
            print ("SALDO : " + str(saldoTemp))       
            print ("----------------------------------")
            print ("")
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
                            linea = ("3" + "," + self.loginDefault + "," + "folio" + "," + pagoId + ","  + str(pagoMonto) + "," + "\n")
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
                                msn = (input("Cuenta Terminada Exitosamente, vuelva pronto !!"))
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
                        f.write("1" + "," + self.loginDefault + "," + "folio" + "," + str(totalDescto) + "," + "V" + "," + "\n")
                        
                        for i in lineaPagos:
                            f.write (i)
                        for i in lineaDetalle:
                            f.write(i)
                        
                        f.close()
                        msn = (input(""))
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
                
                mostrar_lineaProducto = (descripcion + " x " + str(cantidad) + " = " + str(precio))

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

                subtotal = round((subtotal + montoNeto),2)
                total = round((total + pos.calcularImpuesto(montoNeto, impuesto) + montoNeto),2)
                totalImpuesto = round((totalImpuesto + pos.calcularImpuesto(montoNeto,impuesto)),2)
                linea = ("2" 
                + "," 
                + self.loginDefault 
                + "," 
                +"folio" 
                + "," 
                + codigoTemp 
                + "," 
                + str(montoNeto) 
                + "," 
                + str(montoDescto) 
                + "," 
                + "V" 
                + "," 
                + "\n")
                
                lineaDetalle.append(linea)
                break