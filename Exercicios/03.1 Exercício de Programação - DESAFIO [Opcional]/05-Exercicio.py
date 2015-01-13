''' Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321 '''

num = (input ("Digite um Numero : "))

print("Numero inverso : " , num[::-1])


num2 = int(input ("Digite um Numero : "))
invert = 0
while num2 > 0:
    invert *= 10
    invert += num2 % 10
    num2 //= 10
print ("Numero inverso : " , invert)
