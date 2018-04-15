import os
import re 

class usuariosAdministrar (object):
    
    def validarLogin (self, loginValidar):
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

            if (loginValidar == login):
                return (True)
        return (False)
        
    def ingresar (self):
        while True: 
            os.system('cls')
            print ("----------------------------------")
            print ("    Sistema de Punto de Ventas    ")
            print ( "   CREAR/CONSULTAR USUARIOS")
            print ("----------------------------------")
            print ( " ")

            login = ""
            password = ""
            nom = ""
            nivel = 0

            login = (input("Login: "))
            if (login == "0"):
                break

            v = usuariosAdministrar()
            if (v.validarLogin(login) == True):
                x = (input("Este Usuario ya Existe <ENTER>"))
            else: 
                password = (input("Contraseña: "))
                nom = (input("Nombre: " ))
                nivel = (input("Nivel: "))
                login = login.lower()
                password = password.lower()
                nom = nom.lower()

                print (" ")
                opcion = (input("Datos Correctos ?"))
                if (opcion.lower() == "s"):
                        f = open ('usuarios.txt','a')
                        f.write(login + "," + password + "," + nom + "," + nivel + ","+ "\n")
                        f.close()
                        opcion = (input("Datos Guardados Correctamente <ENTER>"))
