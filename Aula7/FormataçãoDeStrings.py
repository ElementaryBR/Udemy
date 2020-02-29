'''
    f'' = f-Strings
    .format(varivael1, varivale2)
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

print('\nnome: {}, idade: {} anos, altura: {}, é maior de idade:? {} IMC = {}'.format(nome,idade,altura,maior_de_idade,imc))


print(f'\nnome: {nome}, idade: {idade} anos, altura: {altura}, é maior de idade:? {maior_de_idade} IMC = {imc:.2f}')

print('\nnome: {}, idade: {} anos, altura: {}, é maior de idade:? {} IMC = {:.2f}'.format(nome,idade,altura,maior_de_idade,imc))


print('\nnome: {0} {0}, idade: {1} anos, altura: {2}, é maior de idade:? {3} IMC = {4:.2f}'.format(nome,idade,altura,maior_de_idade,imc))

print('\nnome: {}, idade: {} anos, altura: {}, é maior de idade:? {} IMC = {:.2f}'.format(nome,idade,altura,maior_de_idade,imc))
