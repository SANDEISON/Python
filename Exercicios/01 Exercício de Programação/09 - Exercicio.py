# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
km_percorridos = float (input ("Informe a quilometragem do carro : "))
qt_dias = int (input ("Informe a quantidade de dias : "))
pagar =(qt_dias*60)+(km_percorridos*0.15)
print ("Valor total a pagar : ", pagar)
