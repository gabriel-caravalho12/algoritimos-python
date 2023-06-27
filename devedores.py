import csv
arquivo = open('arquivos/todos-os-clientes.csv')
arquivodev = open('arquivos/devedores.csv')

clientes = arquivo.read()
devedores = arquivodev.read()


a = set(clientes.split())
b = set(devedores.split())
#
# intersecao = a & b and open('r' 'arquivos/intersecao.csv')
# intersecao.close()
conteudo = a - b

# linhas = conteudo.split(',')
print(conteudo)