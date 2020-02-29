'''
    Operadores Relacionais

==
<
<=
>
>=
!=

'''

print(2 == '2')
print(2 == 2)

n1 = 2
n2 = 2

expressao = n1 == n2
print(f'Igual:{expressao}')

expressao = n1 > n2
print(f'Maior:{expressao}')

expressao = n1 < n2
print(f'Menor:{expressao}')

expressao = n1 != n2
print(f'Diferente:{expressao}')

expressao = n1 >= n2
print(f'Maior ou igual:{expressao}')

expressao = n1 <= n2
print(f'Menor ou igual:{expressao}')

# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# idade_limite = 18
#
#
#
# if idade >= idade_limite:
#     print(f'{nome} pode pegar o empréstimo!!')
# else:
#     print(f'{nome} não podera pegar o emprestimo =(')
#



nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
jovem = 18
idade_ideal = 20
idade_maxima = 30

if idade >= idade_ideal and idade <= idade_maxima:
    print(f'{nome} pode Pegar o empréstimo!!')
else:
    print(f'{nome} não podera pegar o emprestimo =(')