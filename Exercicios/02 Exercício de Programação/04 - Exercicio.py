# Faça um Programa que leia três números e mostre o maior deles.

n1 = input("Digite o 1° numero: ")
n2 = input("Digite o 2° numero: ")
n3 = input("Digite o 3° numero: ")

if (n1 == n2 == n3):
    print ("Todos os numeros são iguais ")  
elif (n1 >= n2) and (n1 >= n3): 
    print (n1, " é o maior numero!! ")
elif( n2 >= n3) :
    print (n2," é o maior numero!!" )
else:
    print (n3,"é o maior numero!!")

   

