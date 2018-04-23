def BPF():
    import os.path
    verificador = os.path.isfile('ventas.txt')
    if verificador == False:
        print('El archivo que contiene los reportes no existía y fue creado.')
        with open('ventas.txt', 'w') as file:
            file.close()
    elif os.stat('ventas.txt').st_size == 0:
        print('Este archivo no contiene información.')
    else:
        with open('ventas.txt') as file:
            contenido = ''
            IF = input('Introduzca la fecha con el siguiente formato (aaaa-mm-dd): ')
            cont = 0
            for linea in file.readlines():
                lista = linea.strip().split(', ')
                if IF in lista[0]:
                    contenido += linea
                    print(linea.strip())
                    cont  +=1
            if cont == 0:
                print('El dato introducido no es válido o no existe.')

        with open('reportefecha.txt', 'w') as file:
            file.write(contenido)