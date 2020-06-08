'''
Operador Ternario
'''

idade = input('Qual a sua idade?: ')

if not idade.isnumeric():
    print('Voce precisa digitar apensa numeros')
else:
    idade = int(idade)
    maior_idade = (idade >= 18)
    mensagem = 'Pode Acessar' if maior_idade else 'Não Pode Acessar'
    print(mensagem)