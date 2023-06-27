import csv

arquivo = open('arquivos/devedores.csv')
conteudo = arquivo.read()
arquivo.close()

linhas = conteudo.split(',')
print(linhas)