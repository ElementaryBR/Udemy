# Criar variaveis para nome, idade , altura, e peso de uma pessoa
# Criar variavel com ano atual
# obter ano de nascimento
# obter IMC com duas casas decimais
# Exibir um texto com todos os valores na tela usando f-strings


nome = 'Ana Flavia'
idade = 25
altura = 1.60
peso = 53
ano_atual = 2020
imc = peso / altura **2
ano_nascimento = ano_atual - idade

print(f'O nome da pessoa é: {nome}\nSua idade é: {idade} anos \nSua altura é: {altura:.2f} metros \nSeu peso é de: {peso}kg\nO ano de Nascimento é: {ano_nascimento}\nE seu IMC é de: {imc:.2f}')

print(f'\n\nO nome da pessoa é: {nome}\nSua idade é: {idade} anos \nSua altura é: {altura:.2f} metros \nSeu peso é de: {peso}kg\nO ano de Nascimento é: {ano_atual-idade}\nE seu IMC é de: {imc:.2f}')