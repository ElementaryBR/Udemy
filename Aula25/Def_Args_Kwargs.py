'''
Funções (def) em Python - * args **kwargs -
Aula 16 (parte 3)
'''

def func(*args):
    print(*args)

var = func(1,2,3,4,5)


def func(*args):
    print(args)

var = func(1,2,3,4,5)


lista = [1,2,3,4,5,6]
n1, n2, *n = lista
print(n1,n2, n)