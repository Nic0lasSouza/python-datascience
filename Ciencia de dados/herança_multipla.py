class Animal:
    def __init__(self, numero_patas) :
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, numero_patas) :
        self.numero_patas = numero_patas
        super().__init__(numero_patas)

class Ave(Animal):
    def __init__(self, numero_patas) :
        self.numero_patas = numero_patas
        super().__init__(numero_patas)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass


class Ornintorrinco(Mamifero, Ave):
    pass

gato = Gato(4)
print(gato)