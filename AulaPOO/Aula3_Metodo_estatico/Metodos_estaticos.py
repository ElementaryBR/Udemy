from random import randint


class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(f'{self.ano_atual - self.idade}')

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimentno):
        idade = cls.ano_atual - ano_nascimentno
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        id = randint(10000, 20000)
        return id


p1 = Pessoa('Junior', 24)
print(p1.gera_id())

p1 = Pessoa.gera_id()
print(p1)
print(Pessoa.gera_id())
