def run():
    edad = int(input('Introduce tu edad: '))

    if edad >= 18:
        print('Hola, eres mayor de edad')
    else:
        print('Hola, eres menor de edad')


if __name__ == '__main__':
    run()