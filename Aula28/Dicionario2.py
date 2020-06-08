d1 = {1:'a', 2:'b', 3:'c'}
v = d1
print(d1)
print(v)

print( v == d1)

v[1] = 'junior'
print(d1)
print(v)

d1 = {1:'a', 2:'b', 3:'c'}
v = d1

v = d1.copy()
v[1] = 'Junior'
print(d1)
print(v)

d1 = {1:'a', 2:'b', 3:'c', 'd': ['Junior','Cardoso']}
print(d1['d'][0])

lista = [
    ('C1',1),
    ('C2',2),
    ('C3',3)
]

d1 = dict(lista)
print(d1)

lista = [
    ['C1',1],
    ['C2',2],
    ['C3',3]
]

d1 = dict(lista)
print(d1)

dicio = {1:2,2:3,4:5}
print(dicio)
dicio.pop(1)
dicio.popitem()
print(dicio)

dicio2 = {4:5,6:7,8:'a'}
dicio.update(dicio2)
print(dicio)
