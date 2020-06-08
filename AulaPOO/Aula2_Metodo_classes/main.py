class Pessoa:
    ano_atual = 2020

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(f'{self.ano_atual - self.idade}')

    @classmethod
    def por_ano_nascimento(cls,nome,ano_nascimentno):
        idade = cls.ano_atual - ano_nascimentno
        return cls(nome, idade)

p1= Pessoa('Junior', 24)
p1.get_ano_nascimento()

p2 = Pessoa.por_ano_nascimento('Junior',1996)
print(p2.nome, p2.idade)