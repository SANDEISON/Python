# Notas e Media

soma = 0
i = 0
nota = []

while i < 4:
    n = float (input ("Digite a Nota : "))
    nota.append (n)    
    i += 1
    soma += n


while i < 4:
    print ( i ," Nota : ", nota [i])    

print ("Média   : ", soma / (i) )

print ("\n\nOutra forma de Imprimir os dados")
print ("Nota : ", nota )    

print ("Média   : ", soma / (i) )
