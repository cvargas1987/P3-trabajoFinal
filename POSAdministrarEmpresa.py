import os
class empresa (object):
    
    def Opcion_Agregar(self):
        import os.path
        valor = False
        while valor == False:
            verificador = os.path.isfile('empresa.txt')
            if verificador == False:
                with open('empresa.txt', 'w') as file:
                    file.close()
                    valor = True
            elif os.stat('empresa.txt').st_size == 0:
                valor = True

            with open ('empresa.txt') as file:
                ID = input('Introduzca el ID de la empresa a agregar: ')
                for linea in file.readlines():
                    lista = linea.strip().split(', ')
                    if ID in lista[0]:
                        valor = False
                    else:
                        valor = True

                if valor == True:
                    nombre = input('Nombre de la empresa: ')
                    ruc = input('RUC de la empresa: ')
                    dc = input('Dirección: ')
                    escribir = open('empresa.txt', 'a+')
                    escribir.write(ID + ', ' + nombre + ', ' + ruc + ', ' + dc + '\n')
                    escribir.close()
                    print('Sucursal agregada con éxito.')
                else:
                    print('Este ID ya existe.')

    def Opcion_Modificar(self):
        import os.path
        verificador = os.path.isfile('empresa.txt')
        if verificador == False:
            print ('Debe agregar una empresa.')
        else:
            with open('empresa.txt') as file:
                contenido = ''
                IDM = input('Introduzca el ID a modificar: ')
                for linea in file:
                    ID = linea[0]
                    if ID in IDM:
                        nombre = input('Introduzca el nombre nuevo: ')
                        RUC = input('Introduzca el nuevo RUC de la empresa: ')
                        DC = input('Introduzca la nueva dirección: ')
                        total = (ID + ', ' + nombre + ', ' + RUC + ', ' + DC + '\n')
                        linea = total
                    contenido += linea
                file.close()
            with open('empresa.txt', 'w') as file:
                file.write(contenido)
                file.close()


    def Opcion_Eliminar(self):
        import os.path
        verificador = os.path.isfile('empresa.txt')
        if verificador == False:
            print('Debe agregar una empresa.')
        else:
            with open('empresa.txt') as file:
                contenido = ''
                IDE = input('Introduzca el ID a eliminar: ')
                for linea in file:
                    lineas = linea.split(',')
                    ID = linea[0]
                    Nombre = linea[1]
                    RUC = linea[2]
                    DC = linea[3]
                    if ID != IDE:
                        contenido += linea
                file.close()
            with open('empresa.txt', 'w') as file:
                file.write(contenido)
                file.close()
                print('Registro eliminado.')

    def Menu_Principal (self):
        os.system('cls')
        print ("----------------------------------")
        print ("    Sistema de Punto de Ventas    ")
        print ( "     PARAMETROS DE EMPRESA")
        print ("----------------------------------")
        print ( " ")
        print ('1. Agregar Sucursarl.')
        print ('2. Modificar Sucursal.')
        print ('3. Eliminar Sucursal.')
        print ('0. Salir')

    def Principal (self):
        while True: 
            Opciones = empresa()
            Opciones.Menu_Principal()
            opcion = input('\t Escoja una opción: ')
            if opcion == "1":
                Opciones.Opcion_Agregar()
            if opcion == "2":
                Opciones.Opcion_Modificar()
            if opcion == "3":
                Opciones.Opcion_Eliminar()
            if opcion == "0":
                return
