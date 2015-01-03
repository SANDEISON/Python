#Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a porcentagem do aumento.
#Exiba o valor do aumento e do novo salário.

salario = float (input ("Digite o valor do salario : "))
porcentagem = float (input ("Digite o valor da porcentagem : "))
aumento = (salario*porcentagem)/100

print ("Total do almento : $" , aumento)
print ("Total do novo salario : $" , (salario + aumento))
