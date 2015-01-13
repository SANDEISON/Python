'''
    A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
    Sua regra de formação é simples: os dois primeiros elementos são 1;
    a partir de então, cada elemento é a soma dos dois anteriores.
    Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci.
    F1 = 1, F2 = 1, F3 = 2, etc.
'''


''' A fórmula de Binet pode ser utilizada para o cálculo do n-ésimo número da sequência de Fibonacci:
Link para o conteudo explicativo : http://www.matematicadidatica.com.br/SequenciaFibonacci.aspx   '''

import math

num = int (input ("Digite um Numero : "))

fibonancci = ( 1.618034 ** num) / math.sqrt(5)

print("Fibonacci : ", round (fibonancci) )
