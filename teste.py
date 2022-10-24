print( "Seja Bem-Vind@ ao brechó três amigos!!!!!!")
print("possuimos camisas, calças e tênis")

peças = input("Qual a peça de roupa você deseja comprar?")
tamanho = input("Qual o tamanho de roupa desejado?")

if peças == "calça":
    print("A calça custa $29,90")
    qtd = int(input("Quantas você deseja?"))
    calça = 29.90
    calculo = calça*qtd
    print(f"{calculo}")
    formapgt = input("Será em dinheiro ou cartão?")
    if formapgt == "dinheiro":
        dinheiro = float(input("quanto foi alcançado:"))
        if dinheiro == calculo :
            print("Sem disponibilidade de troco")
        elif dinheiro >= calculo:
            caltro = dinheiro - calculo
            print(f"Troco de ={caltro}")
        elif calculo >= dinheiro:
            deve = calculo - dinheiro
            print(f"Ainda falta = {deve}")
    elif formapgt == "cartão":
        print("Sera acrescentado um juros de 10%")
        calculocartão =(calculo*qtd)/100
        print(f"Juros no valor de = {calculocartão}")
        senha = int(input("digite sua senha:"))
        print("Compra realizada mediante senha do cartão")

elif peças == "camisa":
    print("A camisa custa $49,90")
    qtd = str(input("Quantas você deseja?"))
    camisa = 49,90
    calculo = camisa*qtd
    print(f"{calculo}")
    formapgt = input("Será em dinheiro ou cartão?")
    if formapgt == "dinheiro":
        dinheiro = float(input("quanto foi alcançado:"))
        if dinheiro == calculo :
            print("Sem disponibilidade de troco")
        elif dinheiro >= calculo:
            caltro = dinheiro - calculo
            print(f"Troco de ={caltro}")
        elif calculo >= dinheiro:
            deve = calculo - dinheiro
            print(f"Ainda falta = {deve}")
    elif formapgt == "cartão":
        print("Sera acrescentado um juros de 10%")
        calculocartão =(calculo*qtd)/100
        print(f"Juros no valor de = {calculocartão}")
        senha = int(input("digite sua senha:"))
        print("Compra realizada mediante senha do cartão")

elif peças == "tênis":
    print("A calça custa $79,90")
    qtd = int(input("Quantas você deseja?"))
    tenis = 79,90
    calculo = tenis*qtd
    print(f"{calculo}")
    formapgt = input("Será em dinheiro ou cartão?")
    if formapgt == "dinheiro":
        dinheiro = float(input("quanto foi alcançado:"))
        if dinheiro == calculo :
            print("Sem disponibilidade de troco")
        elif dinheiro >= calculo:
            caltro = dinheiro - calculo
            print(f"Troco de ={caltro}")
        elif calculo >= dinheiro:
            deve = calculo - dinheiro
            print(f"Ainda falta = {deve}")
    elif formapgt == "cartão":
        print("Sera acrescentado um juros de 10%")
        calculocartão =(calculo*qtd)/100
        print(f"Juros no valor de = {calculocartão}")
        senha = int(input("digite sua senha:"))
        print("Compra realizada mediante senha do cartão")


# preco =float(input("Preço do produto: ") )
# if 0 < preco <= 10.0:
#     desconto = preco * 10 /100
#     print ("Preço inicial: ",preco,"€")
#     print ("Desconto: ",desconto,"€ (10% do inicial)")
#     print ("Total a pagar: ",preco - desconto,"€")
# if preco > 10:
#     desconto = preco * 20 /100
#     print ("Preço inicial: ",preco,"€")
#     print ("Desconto: ",desconto,"€ (20% do inicial)")
#     print ("Total a pagar: ",preco - desconto,"€")
# else:
#     print ("Quantia inválida.")

# print ("Obrigado pela preferência.")
