print( "Seja Bem-Vind@ ao brechó três amigos!!!!!!")
print("possuimos camisas, calças e tênis")

peças = input("Qual a peça de roupa você deseja comprar?")
tamanho = input("Qual o tipo de roupa desejado?")

if peças == "calça":
    print("A calça custa $29,90")
    qtd = input("Quantas você deseja?")
    calça = 29,90
    calculo = calça*qtd
    print(f"{calculo}")
    formapgt = input("Será em dinheiro ou cartão?")
    if formapgt == "dinheiro":
        



preco = float (input ("Preço do produto: ") )
if 0 < preco <= 10.0:
    desconto = preco * 10 /100
    print ("Preço inicial: ",preco,"€")
    print ("Desconto: ",desconto,"€ (10% do inicial)")
    print ("Total a pagar: ",preco - desconto,"€")
if preco > 10:
    desconto = preco * 20 /100
    print ("Preço inicial: ",preco,"€")
    print ("Desconto: ",desconto,"€ (20% do inicial)")
    print ("Total a pagar: ",preco - desconto,"€")
else:
    print ("Quantia inválida.")

print ("Obrigado pela preferência.")
