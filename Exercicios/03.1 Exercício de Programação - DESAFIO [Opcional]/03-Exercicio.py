''' Verifique se um inteiro positivo n é primo.'''

num = int (input ("Digite um Numero : "))

i = 1
cont = 0 

while i <= num :
    if (num % i) == 0:
        cont +=1
    i += 1
if cont == 2:
    print ( num , "É primo ")
else:
    print ( num , "Não é primo ")
