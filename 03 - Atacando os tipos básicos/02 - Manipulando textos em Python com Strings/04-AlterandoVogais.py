#Alterando uma palavra que contem vogais por *

name = input ("Digite uma Palavra ")
i=0
novo = ''
while i < len(name):
    if name[i]in 'aeiou':
        novo =  novo + "*"
    else:
        novo = novo + name[i]    
    i+=1
print(novo)
