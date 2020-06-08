'''
Listas em Python
Fatiamento
append,insert,pop,del,clear,extend,+
min,max
range
'''
lista = ['A','Bacana','C','D','E', 10.5]

print(lista[1])
print(lista)
lista[5] = 'Python'
print(lista)

print(lista[::2])
print(lista[:3])
print(lista[2::2])
print(lista[:])
print(lista[::-1])
print(lista[::-2])

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l3)

l1.extend(l2)# Função extend adiciona como se fosse o append(mas na vdd ela concatena) mas tudo que for alterado no l2 vai ser alterada na lista l1
print(l1)
print(l2)

l1.append(l2)
print(l1)
print(l1[6][2])

l1.insert(0, 'HBSIS Love')
print(l1)
l2.pop(0)
print(l2)
print(l1)

del(l1[2:5])
print(l1)

lista_nova = [1,2,9,11,20,4,3,5,0,6,15]
print(max(lista_nova))
print(min(lista_nova))

print(list(range(0,100,8)))
contador = 0
for valor in lista_nova:
    print(f'Elemento n:{contador} {valor}')
    contador +=1

listas = ['String',True,1,1.5]
for elemento in listas:
    print(f'O tipo de elemento: {elemento} é {type(elemento)}')