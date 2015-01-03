# Considere a empresa de telefonia Tchau.
# Abaixo de 200 minutos, a empresa cobra 0,20 por minuto.
# Entre 200 e 400 minutos. o preço é R$ 0,18.
# Acima de 400 minutos o preço é R$ 0,15.
# Calcule sua conta de telefone.

minutos = int (input("Digite os minutos gastos : "))

if minutos < 200 :
    calc = minutos * 0.20
else:   
    if minutos <= 400:
        calc = minutos * 0.18
    else :
        if minutos <= 800:
            calc = minutos * 0.15
        else :
            calc = minutos * 0.08

print ("Valor a pagar : ", calc)
