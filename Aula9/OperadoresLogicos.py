'''
    Operadores Logicos

and
or
not
in
not in


'''

nome = 'Junior Cardoso'

if 'asdas' not in nome:
    print('Esse texto não existe')
elif 'a' in nome:
    print('Existe')

usuario = input('Nome de usuario:')
senha = input('Senha:')

usuario_bd ='Junin'
senha_bd ='123456'
if usuario == usuario_bd and senha == senha_bd:
    print('Login aceito')
if usuario != usuario_bd:
    print('Login errado')
if senha != senha_bd:
    print('Senha errada')

# Verdadeiro E Falso = Falso
'''comparação1 and comparação2'''
# Verdadeiro E Verdadeiro = Verdadeiro
'''comparação1 and comparação2'''

# Verdadeira OU Verdadeira = Verdadeiro
'''comparação1 or comparação2'''
# Verdadeiro OU Falso = Verdadeiro
'''comparação1 or comparação2'''

a = 2
b = 3

if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')

a = ''
b = 0

if not a:
    print('Favor preencher valor de A')
if not b:
    print('Favor preencher valor de B')

n1 = 0
n2 = 0

if not n1 != n2:
    print('isso')