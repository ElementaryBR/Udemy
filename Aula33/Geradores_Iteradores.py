import sys

def gera():
    for n in range(10000):
        yield n

g = gera()

# for valor in g:
#     print(valor)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
