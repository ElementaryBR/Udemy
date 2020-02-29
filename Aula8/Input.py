'''
    Entrada de dados na tela
utilizando a função input

'''

input('Qual o seu nome?: ')
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
ano_nascimento = 2020 - idade

print(f'{nome} tem {idade} anos. ')
print(f'{nome} nasceu em {ano_nascimento}.')

n1 = int(input('Digite um numero: '))
n2 = input('Digite outro numero: ')

print(f'A soma entre {n1} e {n2} é: {n1+int(n2)}')

variavel = '5.5'
outra = (int(float(variavel))) # primeiro trsnformou a variavel em float depois em int
print(type(outra))
