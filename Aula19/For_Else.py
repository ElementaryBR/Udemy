'''
FOR / ELSE
'''

variavel = ['Junin', 'Miguelzinho', 'Papai','Filhote']

# for valor in variavel:
#     print(valor)
#     continue
#     print(valor)

# for valor in variavel:
#     print(valor)
#     break
#     print(valor)

# for valor in variavel:
#     if valor.startswith('J'):
#         print(f'Tem J em {valor}')
#     elif valor.endswith('e'):
#         print(f'Termina com "e": {valor}')
#     else:
#         print('Não tem nenhuma')

comeca_com_J: False
for valor in variavel:
    if valor.lower().startswith('J'):
        comeca_com_J = True