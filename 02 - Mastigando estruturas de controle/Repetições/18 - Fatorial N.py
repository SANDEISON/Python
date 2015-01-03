# Cálculo do fatorial de 10

i=1
fat = 1
n = int (input ("Digite um número n : "))
while i <= n:
    fat = fat * i
    i = i + 1
print ("Fatorial de %d : %5.2f " %(n , fat))
