# Quantas consoantes foram lidas

name = []
i=1



while i<=10:
    name.append(input("Letra : "))
    i+=1
i=0
cont=0

while i<=9: 
    if name[i] not in 'aeiou':
        cont+=1
    i+=1

print ("Foram lidos %d consoantes" %cont)

