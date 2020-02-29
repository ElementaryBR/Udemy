'''
    Tipos de Dados
str - Strings - Textos
int - inteiro - 12345 0 -5 -200000 7 32
float - real/ponto flutuante - 10.5 20.2 0.0 -5.0
bool - booleano/lógico - True/False (10 == 10)
'''

print('Junior')
print(type('Junior'))
print('Junior', type('Junior'))
print('10' ,type('10'))
print(10, type(10))
print('String' == "String" ,type('String' == "String")) #com uma aspas ou duas, de toda forma são iguais
print(10 == 10, type(10 == 10))
print(False, type(False))
print(5.0, type(5.0))

# Type Casting / Conversão de tipos

print('\n',5.0, type(5.0) , bool(5.0),sep='')
print(5.0, type(5.0), int(5.0))
# print('Junior', type('Junior'), int('Junior')) # assim dara erro pq não tem como converter uma string com caracteres em um numerio inteiro
print('5.0', type('5.0'), int('5.0'))
