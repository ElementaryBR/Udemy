def funcao(arg,arg2):
     return arg * arg2

print(funcao(2,2))

a = lambda x, y: x * y
print(a(2,2))


def outra_funcao(arg):
    return arg

print(outra_funcao(a))

lista_produtos = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]

def ordenar_por_item(item):
    return item[1]

lista_produtos.sort(key=ordenar_por_item)
print(lista_produtos)

def ordenar_por_item(item):
    return item[1]

lista_produtos.sort(key=ordenar_por_item, reverse= True)
print(lista_produtos)

lista_produtos.sort(key=lambda item: item[1], reverse= True)
print(lista_produtos)

print(sorted(lista_produtos, key=lambda item:item[1], reverse=True))
print(sorted(lista_produtos, key=lambda item:item[0]))