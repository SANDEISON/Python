# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
qt_cigarros = int (input ("Informe a quantidade de cigarros fumados por dia : "))
qt_anos = int (input ("Informe a quantidade de anos : "))
total_cigarros = (qt_anos*365)* qt_cigarros
total_minutos=(total_cigarros*10)
perda_dias= (total_minutos//24) # esta armazenando a parte inteira de divisão

print ("O total de dias perdidos foram = ", perda_dias)
