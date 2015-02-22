#Importanto o modulo randomico
import random

print("Imprimindo as funções do modulo random ")
print (dir(random))

print("Imprimindo um HELP das funções")
print (help(random.randint))

print("Imprimindo um numero aleatorio de 1 ate 100")
print (random.randint(1,100))

print("Imprimindo um HELP das funções")
print (help(random.choice))

print("Escolhendo um elemento de uma Lista ")

print (random.choice(['sao paulo', 'santos', 'palmeiras', 'csa', 'crb' ]))
