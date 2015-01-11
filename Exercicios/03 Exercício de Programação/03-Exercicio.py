'''
    Supondo que a população de um país A seja da ordem de 80000 habitantes
    com uma taxa anual de crescimento de 3% e que a população de B
    seja 200000 habitantes com uma taxa de crescimento de 1.5%.
    Faça um programa que calcule e escreva o número de anos necessários
    para que a população do país A ultrapasse ou iguale a população do país B,
    mantidas as taxas de crescimento
'''

pais_A = 80000
pais_B = 200000
qtAnos = 0

while (pais_A < pais_B):
    crescimento_A = 0.3 * pais_A
    crescimento_B = 0.015 *pais_B
    pais_A += crescimento_A
    pais_B += crescimento_B
    qtAnos += 1

print("Quantidades de Anos : %d " %qtAnos)
