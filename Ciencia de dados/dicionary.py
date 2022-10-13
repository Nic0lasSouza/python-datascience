pessoa = {"Nome": "Guilherme", "Idade": 28}
pessoa = dict(nome="Guilherme", Idade=28)
pessoa["telefone"] = "3333-1234"
print(pessoa)

dados = {"Nome": "Guilherme", "Idade": 28, "Telefone":"3333-1234"}
print(dados["Nome"])
print(dados["Idade"])
print(dados["Telefone"])

dados["Nome"] = "Maria"
dados["Idade"] = 18
dados["Telefone"] = "9988-1781"

print(dados)

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone":"5552-2569"},
    "giovani@gmail.com": {"nome": "Giovani", "telefone": "3656-5789"},
    "chaplin@gmail.com": {"nome": "chaplin", "telefone":"3654-5821"},
    "rafa@gmail.com": {"nome": "rafaela" , "telefone": "4455-6583", "extra": {"a":1}},
}
telefone = contatos["giovani@gmail.com"]["telefone"]
print(telefone)

extra = contatos["rafa@gmail.com"]["extra"]["a"]
print(extra)

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave ,valor)