

'''
Crie uma função que recebe uma função2 como parametro e retonre o valor da função2 executada
'''

"""
2 Crie uma função 1 que recebe uma função 2 como parametro  e retorne o valor da função2 executada
Faça a funçao1 executar duas funções que recebam um numero difrente de argumentos.
"""

# Exercicio 1
def funcao1(outra_funcao):
    return outra_funcao

def funcao2():
     return 'Ola Muito Prazer'

variavel_da_funcao2 = funcao2()

print(funcao1(variavel_da_funcao2))


# Exercicio 2

def pessoa(nome):
    return f'Olá {nome}'

def saudacao(nome, saudacao):
    return f'{nome}  {saudacao}'

def funcao_mestra(funcao):
    return funcao

var = funcao_mestra(pessoa(saudacao('Junior, ', 'prazer em conhece-lo')))
print(var)



# OOU


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando)
print(executando2)