# Cálculo da soma de 10 números inteiros


soma = 0

while True:
    x = int ( input ( "Digite um número : " ))
    print ("Digite  0 para sair \n\n")
    if x == 0:
        break
    
    soma = soma + x
    
print ("Soma : %d : " %soma)
