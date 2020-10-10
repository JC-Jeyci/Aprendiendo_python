conversion = input('''Opciones de conversion
[1] Convertir dolar a peso mexicano
[2] Convertir peso mexicano a dolar
Por favor ingresa una opcion:
''')
try:
    conversion = int(conversion)

    if conversion == 1:
        valor_mx = 0.047
        pesos = input("¿Cuantos dolares tienes ?:")
        pesos = float(pesos)
        dolares = pesos / valor_mx
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print("Tienes $" + dolares + " en pesos mexicanos")
    else:
        valor_dolar = 21.46
        pesos = input("¿Cuantos pesos mexicanos tienes ?:")
        pesos = float(pesos)
        dolares = pesos / valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print("Tienes $" + dolares + " en dolares")
except :
    print('* * * * * * E R R O R * * * * * *')
    print('Por favor, Ingresa solo valores numericos')




