'''
CONTADORES
E
ACUMULADORES

'''


contador = 1
acumulador = 1
while contador <=5:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('A condição ficou False')