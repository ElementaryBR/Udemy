t1 = (1, 2, 3, 'a', 'Junior\n')

print(t1)
print(t1[2])
print(t1[-1])

for elemento in t1:
    print(elemento)

t2 = 1,2,3,'a','Junior'
print(t2)

t3 = 1
print(t3)
t3 = 1,
print(t3)

t4 = t1 + t2
print(t4)

n1, n2, n3, *_ = t1
print(n1)
print(n2)
print(n3)
print(_)

t1 = list(t1)
print(t1)
t1 = tuple(t1)
print(t1)
