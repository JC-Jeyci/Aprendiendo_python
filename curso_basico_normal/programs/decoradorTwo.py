# -*- coding: utf-8 -*-

def funcion_decorador(funcion_parametro):
    
    def nombrePersona(nombre):
        if nombre != '':
            print('hola {}'.format(nombre))

            #Se puede emviar el parametro a la funcion secundaria
            #funcion_parametro(nombre) 

            #Se puede omitir el parametro en la funcion secundaria
            funcion_parametro()
        else:
            print('No hay programador')

    return nombrePersona

'''
En este ejemplo se envia el nombre a la funcion directamente para utlizarlo despues
@funcion_decorador
def saludar(nombre):
    print('soy un programador, {}'.format(nombre))
'''

'''
Tambien se puede omitir el parametro aunqe en la instancia del metodo se este enviando el parametro
'''
@funcion_decorador
def saludar():
    print('soy un programador, {}'.format(nombre))


if __name__ == '__main__':
    print('F U N C I O N E S  C O N  D E C O R A D O R')

    nombre = str(input('Introduce tu nombre: '))

    saludar(nombre)