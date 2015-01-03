'''
Faça um Programa que peça os três lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo,
se o mesmo é: equilátero, isósceles ou escaleno.
'''


a = int (input ("Digite o 1° Lado ") )
b = int (input ("Digite o 2° Lado ") )
c = int (input ("Digite o 3° Lado ") )



#Verificamos a existencia de um triângulo

if ( ( (b-c) < a < b+c ) and ( (a-c) < b < a+c ) and ( (a-b) < c < a + b )):
     print ("Os valores formam um triângulo")
     if (a==b==c):
         print("Triângulo Equilátero")
     elif (a!=b!=c):
        print ("Triângulo Escaleno ")
     else:
         print ("Triângulo isorceles")
else:
    print("Os valores não formam um triângulo")
    
