usuario = input('Digite seu usuario: ')
qtd_caracters = len(usuario)

print(f'{usuario}, {qtd_caracters},{type(qtd_caracters)}')

if qtd_caracters <  6:
    print('Voce precisa cadastrar mais de 6 caracteres')
else:
    print('Cadastrado')

n1 = input('Digite alguma coisa: ')
n2 = input('Digite outra coisa: ')

print(f'a quantidade de caracteres digitados foram {len(n1)+len(n2)}')

