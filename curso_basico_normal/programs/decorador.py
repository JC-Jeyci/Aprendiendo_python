# -*- coding: utf-8 -*-

def funcion_decoradora(funcion_parametro):

    def funcion_interior():
        print('Enviar saludos')

        funcion_parametro()

    return funcion_interior


@funcion_decoradora
def mensaje():
    print('Hola programador en python')



if __name__ == '__main__':
    print('F U N C I O N E S  C O N  D E C O R A D O R')

    mensaje()