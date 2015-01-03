# Cálculo da media de 10 números

num = 0
i=1
media = 0
while i <= 10:
    num = int (input ("Digite o %d ° número " % i) )
    media = media + num
    i = i + 1
print ("Média dos números : %5.2f " %  media/10)
