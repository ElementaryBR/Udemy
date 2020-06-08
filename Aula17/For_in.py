'''
For in em Python
Iteradno strings com for
Função range(start=0, stop, step =1)

'''

# texto = 'Python'
# for n, letra in enumerate(texto):
#     print(n, letra)

for numero in range(2,10,2): #Função range(start=0, stop, step =1)
    print(numero)

for numero in range(20,10,-1):  #Função range(start=0, stop, step =1)
    print(numero)

for n in range(100):
    if n % 8 == 0:
        print(n)