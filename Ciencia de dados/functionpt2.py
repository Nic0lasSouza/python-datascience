from traceback import print_tb
from unittest import result


def criar_carro(modelo, ano, placa, /, marca, motor,combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="fiat", motor="1.0", combustivel="gasolina")

def somar(a,b):
    return a+b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação {a}+{b}={resultado}")

exibir_resultado(10,10, somar)

salario = 2000
def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus
    return salario
lista = [1]
novo_salario = salario_bonus(500, lista)
print(novo_salario)
print(lista)