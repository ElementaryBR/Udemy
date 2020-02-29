'''

#### Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario não digite um numero inteiro, informe que não é um
numero inteiro


############################################################################################################

Faça um programa que pergunte a hora ao usuario e basenado-se no horario
descrito, exiba a saudação apropriada. EX
Bom Dia 0 - 11, Boa Tarde 12-17 e Boa Noite 18-23

############################################################################################################

Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"
Se tiver entre 5 e 6 letras "seu nome é normal", e se for maior que 6 "Seu nome é muito grande"


'''

try:
    n1 = int(input('Digite um numero inteiro: '))
    if n1 == int(n1):
        print('Isso ai você sabe o que é um numero inteiro')
        print(f'O numero digitado foi {n1}')
    if (n1 % 2):
        print(f'{n1} é um numero impar')
    else:
         print(f'{n1} é um numero par')
except:
    print('Por Favor digite apenas um numero inteiro!!')

horario = input('Digite o horario atual: ')
dia = ['00','01','02','03','04','05','06','07','08','09','10','11']
tarde = ['12','13','14','15','16','17']
noite = ['18','19','20','21','22','23']

if horario[:2] in tarde:
    print('Boa Tarde')
elif horario[:2] in noite:
    print('Boa Noite')
elif horario[:2] in dia:
    print('Bom Dia')

nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print('Você tem um nome muito curto')
elif len(nome) >4 and len(nome) <=6:
    print('Você tem um nome normal')
elif len(nome) > 6:
    print('Você tem um nome muito grande')
