l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [ v for v in l1]
print(ex1)
ex2 = [v *2 for v in l1]
print(ex2)
ex3 = [(v,c) for v in l1 for c in range(3)]
print(ex3)


l2 = ['Junior', 'Miguel', 'Clorofila']
ex4 = [v.replace('o', '#').upper() for v in l2]
print(ex4)

tupla = (
    ('Chave', 'Valor'),
    ('Chave2', 'Valor2')
)
ex5 = [(y,x) for x,y in tupla]
print(ex5)
ex5 = dict(tupla)
print(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0]
print(ex6)

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex7)
