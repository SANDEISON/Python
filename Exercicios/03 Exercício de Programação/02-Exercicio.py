''' Faça um programa que leia um nome de usuário e a sua senha e
    não aceite a senha igual ao nome do usuário,
    mostrando uma mensagem de erro e voltando a pedir as informações.
'''

name = input ("Nome de Usario:")
senha = input ("Senha: ")

while senha == name:
    print("A senha não pode ser igual ao nome !!!")
    name = input ("Nome de Usario:")
    senha = input ("Senha: ")
