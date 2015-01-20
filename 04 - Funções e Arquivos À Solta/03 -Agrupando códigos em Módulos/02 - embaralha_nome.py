def embaralha (x):
    import random
    lista = list(x)
    random.shuffle(lista)
    return ''.join(lista)
    
nome = input ("Digite algum nome : ")
print (embaralha(nome))
