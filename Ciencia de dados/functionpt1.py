def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônino"):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2(nome = "Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1
    return antecessor, sucessor

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro Inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca":"Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of python", "Beautiful is beter than ugly.", autor = "Tim peters", ano= 1999)