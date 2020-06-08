# add (adiciona), update(atualiza), clear, discard
# union | (une)
# inserction & (todos os elementos presents nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

s1 = {1,2,3,4,5,6}
s1.update((15,20,'Junior'))
print(s1)

s2 = set()
s2.add(1)
s2.add(2)
s2.add(7)
s2.add((1,2,3,'Junior'))
print(s2)

s3 = s1 | s2
print(s3)

s4 = s3 & s1
print(s4)

s4 = s1 - s2
print(s4)

s4 = s1 ^ s2
print(s4)
print(type(s4))
s4 = s1.discard(1)
print(s4)

l1 = [1,2,3,3,3,3,3,2,4,5,6,7,8,8,8,9,10,'Jiai','Jasd']
print(l1)
l1 = set(l1)
print(l1)
l1 = list(l1)
print(l1)
