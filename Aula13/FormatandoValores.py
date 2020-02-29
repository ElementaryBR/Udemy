'''
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Numero de ponto flutuante (float)
:.(numero)f - quantidade de casas decimais (float)
:(caractere)(> ou < ou ^) (Quantidade) (Tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

'''

n1 = 10
n2 = 3
divisao = n1 / n2

nome = "Juninho"
print(f'{divisao:.2f}')
print(f'{nome:s}')
print(f'{n1:d}')

print(f'{nome:$^10}')
print(f'{nome:$>10}')
print(f'{nome:$<10}')
nome2 = 'HBSIS'
nome2 = nome2.ljust(20, '%')
print(nome2)
nome = nome.rjust(20, '@')
print(f'Nome: {nome}\n')

outro_nome = 'juNior'

print(outro_nome.lower()) # minusculo
print(outro_nome.upper()) # maiuscula
print(outro_nome.title()) # Primeira letra minuscula