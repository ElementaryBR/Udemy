'''
    Laços de repetição - While

utilizado para realizar ações enquanto um condição for verdadeira



'''

# while True: # loop infinito
#     nome = input('Qual o seu nome?')
#     print(f'Olá {nome} !')

x = 0
print(x)
while x <= 100:
    print(x)
    x += 1
    # ou x = x + 1

print('Fim do laço')

# x = 0
# while x <= 100:
#     continue
#
#     print(x)
#     x += 1
# print('Fim do laço')

x = 0
while x <= 100:
    if x == 3:
        x += 1
        print(x)
        continue

    print(x)
    x += 1


print('Fim do laço')

x = 0
while x <= 100:
    if x == 3:
        x += 1
        print(x)
        break

    print(x)
    x += 1 


print('Fim do laço')