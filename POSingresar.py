import re
import os
import POSmenuPrincipal


class validar (object):
    def __init__(self, loginValidar, passwordValidar):
        self.loginValidar = loginValidar
        self.passwordValidar = passwordValidar

    def validarLogin (self):
        
        if (self.loginValidar == "root" and self.passwordValidar == "123123"):
                return ("admin")
                
        try:
            f = open('usuarios.txt','r')
        except FileNotFoundError:
            print ("--> ERROR!! No Existe Archivo de Usuarios")  
            return (False) 

        for linea in f.readlines():

            linea = linea.split(',')
            login = linea[0]
            password = linea [1]
            nombre = linea [2]
            nivel = linea [3]

            if (self.loginValidar == login):
                if (self.passwordValidar== password):
                    return (nombre)
        return (False)
        

if __name__ == '__main__':
    while True: 
        os.system('cls')
        print ("----------------------------------")
        print (chr(27)+"[1;33m"+"    Sistema de Punto de Ventas    ")
        print ( "        INICIAR SESION")
        print ("----------------------------------")
        
        loginValidar = (input("LOGIN     : "))
        passwordValidar = (input("CONTRASENA: "))
        v = validar(loginValidar,passwordValidar)
        if (v.validarLogin() is not False):
            print ("")
            x = (input("<<<< Bienvenido " +  v.validarLogin() + "!! >>>>"))
            POSmenuPrincipal.menuPrincipal()

            