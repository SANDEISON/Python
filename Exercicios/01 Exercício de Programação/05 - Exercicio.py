# Solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

preco_mercadoria = float (input ("Digite o valor da mercadoria : "))
percentual_desconto = float (input ("Digite o percentual de desconto : "))
desconto = (preco_mercadoria*percentual_desconto)/100

print ("Percentual de desconto : $" , desconto)
print ("Preço a pagar : $" , (preco_mercadoria - desconto))
