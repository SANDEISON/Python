#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e imprma com o nome do mes por extenso.

mes = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO","AGOSTO"
       ,"SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"]



data = input ("Digite a data dd/mm/aaaa :")
num = int(data[3:5])

print(num)

print (data[0:2]," de ", mes[num-1], " de ", data[6:])
