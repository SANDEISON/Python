# Verificando String's
arquivo = "exemplo.py"

# Verifica se inicia com 'e'
print (arquivo.startswith('e'))

#Verificar se termina com "py"

print (arquivo.endswith('py'))

resposta = "Sim"
print ("Deixando tudo Maiuscula : ", resposta.upper())

print ("Deixando tudo menuscula : ", resposta.lower())


# Buscando texto em uma frase
frase ="Um tigre, dois tigres, tres tigres, estão juntos .  "

#busca uma string dentro do texto
# mostra o indice onde inicia a string
#caso não encontre mostrara -1
print (frase.find("dois"))


# Busca a string a partir de um indice
print (frase.find("tigre",30))


# Alterando um texto na frase
frase = frase.replace("tigre","pato")

print (frase)

# split = separa ,  join = junta
txt = "Batatinha quando nasce"
print (txt.split())

data = "09/01/2015"
print (data.split("/"))

ip = "192.168.1.1"
print (ip.split("."))



times = ["Sao Paulo","santos"," vitoria"]
print ("/".join(times))















