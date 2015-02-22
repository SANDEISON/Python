arq = open("Alice.txt") # Abrindo o arquivo
texto = arq.read() # Lendo todo o arquivo
texto = texto.lower() # converte para menusculos
import string  # Importando a biblioteca de Strings

for c in string.punctuation:
    texto = texto.replace(c," ") # Troca o 'c' por espaço
texto = texto.split() # Separa as palavras

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p]+=1

print ("Alice aparece %s vezes" %dic["alice"])
arq.close() #Fechando o arquivo
