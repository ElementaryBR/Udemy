def soma(x,y):
    assert isinstance(x, (int,float)), 'x precisa ser inteiro ou float'
    assert isinstance(y, (int,float)), 'y precisa ser inteiro ou float'
    return x + y
try:
    print(soma('3',2))
except AssertionError as e:
    print(f'Conta invalida: {e}')
try:
    print(soma(2,'4'))
except AssertionError as e:
    print(f'Conta invalida: {e}')

try:
    print(soma(2,2))
except AssertionError as e:
    print(f'Conta invalida: {e}')
