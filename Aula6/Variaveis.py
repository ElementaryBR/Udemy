'''
variavel = qualquer coisa

o sinal de igual é representado por atribuir
nome = 'Junior'
a string 'Junior'
esta sendo atribuida a variavel nome
ou seja a variavel nome tem o valor de 'Junior'


'''

nome = 'Junior Cardoso'
idade = 23
altura = 1.69
peso = 70
maior_de_idade = idade >= 18
imc = peso / (altura*altura)
# ou imc = peso/ altura ** 2

print(f'nome: {nome}, idade: {idade} anos, altura: {altura}, é maior de idade:? {maior_de_idade}')

print(f'\nnome: {nome}, idade: {idade} anos, altura: {altura}, é maior de idade:? {maior_de_idade} IMC = {imc}')
