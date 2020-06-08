

class A:
    vc = 123

class B:
    vc = 123

a1 = A()
a2 = A()
print(a1.vc)
print(a2.vc)
print(A.vc)

b1 = B()
b2 = B()
B.vc = 321
print(b1.vc)
print(b2.vc)
print(B.vc)
