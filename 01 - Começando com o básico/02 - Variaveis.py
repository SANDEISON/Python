# Declarando Variaveis

my_variable = 10 # inteiro
my_variable2 = 15.5 #float
my_variable3 = "Sandeison" #string

print ( "Variavel 1 :  ", my_variable )
print ( "Variavel 2 :  ", my_variable2 )
print ( "Variavel 3 :  ", my_variable3 )


print ( "Retornando o endereço de memoria")
print ( "Variavel 1 :  ", id (my_variable) )
print ( "Variavel 1 :  ", id (10) )

print ( "Variavel 2 :  ", id (my_variable2) )
print ( "Variavel 2 :  ", id (15.5) )

print ( "Variavel 3 :  ", id (my_variable3) )
print ( "Variavel 3 :  ", id ("Sandeison") )

print ( "\n\n Retornando os metodos de um objeto ")

print ( "Variavel 3 :  ", dir("Sandeison") )

print ( "\n\n Help  do metodo do objeto")

print ( "Variavel 3 :  ", help ("Sandeison".upper ) )
