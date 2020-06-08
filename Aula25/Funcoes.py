'''
Funções - def em Python (parte 1)
'''

def funcao(nome):
    print('Hello World')
    nome = nome.replace('e','3')
    return f'{nome}'

funcao('Fiquei em Casa')
var = funcao('Fiquei em Casa')
print(var)


def conta_porcentagem(n1,n2):
    return (n2/100) * n1 + n1
print(conta_porcentagem(100,10))

def fizzbuzz(n1):
    if n1 %2 == 0:
        return 'Fizz'
    elif n1 %5 == 0:
        return 'Buzz'
    elif n1 %5 == 0 and n1 %3 == 0:
        return 'FizzBuzz'
    else:
        return n1

print(fizzbuzz(9))