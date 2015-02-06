import random
lista = []

while len(lista) < 15:
    x = random.randint(10,100)
    if x not in lista:
        lista.append(x)
# coloca em ordem crescente
lista.sort() 
print(lista)
