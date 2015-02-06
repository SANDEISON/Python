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


# Imprimindo os dados do arquivo

arquivo = open("numeros.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

