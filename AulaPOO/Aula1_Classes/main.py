from AulaPOO.Aula1_Classes.pessoa import Pessoa

p1 = Pessoa('Junior', 24)
p2 = Pessoa('Ana',19)
p1.comer('carne')
p1.falar('corona')
p1.parar_de_comer()
p1.falar('corona')
p1.falar('bolsonaro')
p1.comer('pao')
p1.parar_de_comer()
p1.parar_de_falar()
p1.comer('pao')

print(p1.ano_atual)

print(p1.ano_nascimento())
print(p2.ano_nascimento())
