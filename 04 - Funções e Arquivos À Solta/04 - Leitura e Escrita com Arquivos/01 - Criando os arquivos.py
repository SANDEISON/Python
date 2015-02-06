'''
    A função que abre o arquivo é open
    e os modulos são :
    r - leitura
    w - escrita
    a - append
    b - binario
    + - atualização
    os arquivos devem ser fechados com close


'''

'''
    criando o primeiro arquivo no diretorio central
    o arquivo é criado onde o programa esta salvo
'''

arquivo = open("numeros.txt", "w")# o "w" cria um novo arquivo , cao ja exista o arquivo é sobrescrito
for linha in range(1,101):
    arquivo.write("%d\n" %linha)
arquivo.close()
