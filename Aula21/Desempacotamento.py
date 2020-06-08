'''
Desempacotamento de listas em Python
'''

lista = ['Junin', 'Miguel', 'Ana']

n1, n2, n3 = lista

print(lista,n1,n2)

lista = ['Junin', 'Miguel', 'Ana']

n1, n2, *outra_lista = lista
print(lista,n1,n2)
print(outra_lista)

lista = ['Junin', 'Miguel', 'Ana']

*outra_lista, n1, n2 = lista
print(n1)
print(n2)
print(outra_lista)