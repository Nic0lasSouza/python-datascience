potuacao = 0
x =0
soma = potuacao+x
print("Bem vindo ao jogo de escolhas desenvolvido em python")
print("Quanto é 7+7÷7+7*7-7=")
print(("(A)00    (B)08    (C)50   (D)56"))
pergunta1= input()
if (pergunta1 == "C"):
    print("Acertou miseravi!")
    x +=1
else:
    print("Você errou")


print("1+4 = 10")
print("4+16= 40")
print("2+8= 20")
print("8+32 = ?????")
print("Qual é o resultado da operação que contém ???")
pergunta2=input()
if (pergunta2 == "80"):
    print("Você acertou!")
    x +=1
else:
    print("Você errou")


print("Quanto é 5*2+1*0")
print("a)7     b)9    c)8   d)10")
pergunta3 = input()
if (pergunta3 == "D"):
    print("Você acertou!")
    x +=1
else:
    print("Você errou")

print("A + A= 30")
print("B + B= 20 ")
print("C + C= 8")
print("A + B *C= ?")
print("Qual o resultado?")
pergunta4 = input()
if (pergunta4 == "45"):
    print("Você acertou !")
else:
    print("Você errou")

print("Qual deles tem dois zero dois quatro")
print("a)0044      b)0024   c)2024")
pergunta5 = input()
if (pergunta5 == "C"):
    print("Acertou miseravi")
    x +=1
else:
    print("Você está bem ? errando")

print("Quanto é 1+1 ?")
print("a)-3")
print("b) 5!- 3!")
print("c) 2(2-1)")
print("6-(-4)")
pergunta6 = input()
if (pergunta6 == "C"):
    print("Acertou")
    x +=1
else:
    print("Errou")

print("Qual é o seguinte número?")
print("89547")
pergunta7 = input()
if (pergunta7 == "6"):
    print("Acertou")
    x +=1
else:
    print("Errou")

print("Qual  a reposta correta para a resolução desta expressão:")
print("4*4")
print("a)1  b)16")
pergunta8 = input()
if (pergunta8 == "B"):
    print("Acertou")
    x+=1
else:
    print("errou de novo")

print("2+6/2*3")
print("a)11     b) 1,33     c)3     d)12")
pergunta9 = input()
if (pergunta9 == "C"):
    print("Acertou")
    x+=1
else:
    print("errou")

print("Qual o resultado?")
print("-3+3*3+3/3+3")
print("a)0     b)1      c)3     d)4     e)10")
pergunta10 = input()
if(pergunta10 == "E"):
    print("Acertou")
    x+=1
else:
    print("Errou")

print(f'Resultado: {x} Acertos')

