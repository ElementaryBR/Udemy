'''
Iterando strings com while

'''

minha_string = 'o rato roeu a roupa do rei de roma.'
tama_str = len(minha_string)

# print(minha_string[2])
c= 0
# while c <= tama_str:
#     print(minha_string[c])
#     c += 1

# nova_str = ''
# while c < tama_str:
#
#     if minha_string[c] == 'r':
#         nova_str = nova_str + minha_string[c].upper()
#     else:
#         nova_str += minha_string[c]
#         print(nova_str)
#
#     c += 1
# print(nova_str)

nova_str = ''
c = 0
contagem_atual = 0
letra = ''
while c < tama_str:
    qtd_vzs_letra = minha_string.count(minha_string[c])
    if contagem_atual < qtd_vzs_letra and minha_string[c].strip():
        letra = minha_string[c]
        contagem_atual = qtd_vzs_letra

    c += 1

print(letra, contagem_atual)