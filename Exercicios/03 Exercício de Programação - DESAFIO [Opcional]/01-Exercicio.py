''' Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
    Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.
'''

num = int (input ("Digite um Numero : "))

triangular = 0
cont = 2

while triangular < num:    
    triangular = cont * (cont + 1 )* (cont + 2)    
    cont += 1
    
if (triangular == num):
    print ("É triangular")
else :
    print ("Não é triangular")
