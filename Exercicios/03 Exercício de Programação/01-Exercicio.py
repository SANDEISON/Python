'''
    1. Faça um programa que peça uma nota, entre zero e dez.
    Mostre uma mensagem caso o valor seja inválido e
    continue pedindo até que o usuário informe um valor válido.
'''

num = -1
while (num < 0) or (num > 10):
    num = float(input("Digiete um Numero  entre 0 e 10: "))
     
