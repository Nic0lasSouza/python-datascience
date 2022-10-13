from typing_extensions import Self


class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("ZZZZzzzzzz....")

cao_1 = Cachorro("chappie", "amarelo", False)
cao_2 = Cachorro("Aladim", "branco e preto")

cao_1.latir()
print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)