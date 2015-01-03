# Multa de Transito
# Pergunte a velocidade de um caro, supondo um valor inteiro.
# Caso ultrapase 110 km/h, exiba a mensagem dizendo que o usuário
# foi multado. Nesse caso, exiba o valor da multa, cobando R$ 5,00
# por km acima de 110,00.

velocidade = int(input("Digite a velocidade do carro : "))

if velocidade <= 110 :
    print("Seu carro não foi multado!")
if velocidade > 110 :
    print ("Seu carro foi multador ! ")
    multa = (velocidade - 110) * 5
    print("Valor da Multa : ", multa)
