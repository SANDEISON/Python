'''

    Dados dois números inteiros positivos,
    determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.

'''

num1 = int (input ("Digite o 1 numero :"))
num2 = int (input ("Digite o 2 numero :"))

verifica = num1 % num2
mmc = 1
while (verifica != 0):


    verifica = num1 % num2
    mmc = num1 % num2
    num1 = num2
    num2 = mmc
    
print (mmc)
    
