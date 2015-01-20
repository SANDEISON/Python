# Ordem Inversa

soma = 0
i = 0
vetor = []

while i < 10:
    n = float (input ("Digite um Número : "))
    vetor.append (n)    
    i += 1


while i > 0 :   
    print ("Vetor ", i ," : ", vetor[i-1])
    i = i - 1
