numeros = set([1, 2, 3, 1, 3, 4])
letras = set("abacaxi")
carros = {"palio", "gol", "celta"}
print(letras)
numeros = list(numeros)
print(numeros[0])

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))

conjunto_a1 = {1, 2, 3}
conjunto_b1 = {4, 1, 2, 5, 6, 3}
print(conjunto_a1.issubset(conjunto_b1))
print(conjunto_b1.issubset(conjunto_a1))

conjunto_a2 = {1, 2, 3, 4, 5}
conjunto_b2= {6, 7, 8, 9}
conjunto_c2 = {1,0}

print(conjunto_a2.isdisjoint(conjunto_b2))
print(conjunto_a2.isdisjoint(conjunto_c2))
