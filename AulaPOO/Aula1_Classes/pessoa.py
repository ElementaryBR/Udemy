from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não pode falar enquanto come')
            return
        if self.comendo:
            print(f'{self.nome} ja esta comendo')
            return
        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True

    def falar(self,assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto come')
            return
        if self.falando:
            print(f'{self.nome} ja esta falando.')
            return
        print(f'{self.nome} começou a falar sobre {assunto}')
        self.falando = True

    def parar_de_falar(self):
        if self.falando == False:
            print(f'{self.nome} ja não esta mais falando.')
            return
        print(f'{self.nome} parou de falar. ')
        self.falando = False

    def parar_de_comer(self):
        if self.comendo == False:
            print(f'{self.nome} ja não esta mais comendo. ')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def ano_nascimento(self):
        return self.ano_atual - self.idade