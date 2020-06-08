n1 = 10
n2 = 0
while not n1 == 1:
    print(n2,n1)
    n1 = n1 - 1
    n2 = n2 + 1

print('\nJeito dois\n')

contador = 10
for valor in range(10):
    print(valor,contador)
    contador -= 1

for r in range(10,1,-1):
    print(r)

for p, r in enumerate(range(10,1,-1)):
    print(p,r)