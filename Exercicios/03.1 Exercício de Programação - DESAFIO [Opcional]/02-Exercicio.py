''' Indique como um troco deve ser dado utilizando-se um número mínimo de notas.
    Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos.
    Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.
'''

conta = int (input ("Valor a ser pago : "))
pagamento = int (input ("Valor pago : "))
notas = [0,0,0,0,0,0]

verifica = pagamento - conta

while verifica > 0:

    if verifica >= 50:
        verifica -= 50
        notas [5]+= 1
    elif verifica >= 20:
        verifica -= 20
        notas [4]+= 1
    elif verifica >= 10:
        verifica -= 10
        notas [3]+= 1
    elif verifica >= 5:
        verifica -= 5
        notas [2]+= 1
    elif verifica >= 2:
        verifica -= 2
        notas [1]+= 1
    else:
        verifica -= 1
        notas [0]+= 1
       
print ("TROCO ")
print ("50 : ", notas[5])
print ("20 : ", notas[4])
print ("10 : ", notas[3])
print ("5  : ", notas[2])
print ("2  : ", notas[1])
print ("1  : ", notas[0])
