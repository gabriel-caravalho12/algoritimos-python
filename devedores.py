import csv
arquivo = open('arquivos/todos-os-clientes.csv')
arquivodev = open('arquivos/devedores.csv')


clientes = arquivo.read()
devedores = arquivodev.read()

# cli_list = list(clientes)

a = set(clientes.split())
b = set(devedores.split())
#
intersecao = a - b
nov_intersecao = list(intersecao)

nome = nov_intersecao[0]
nao_devedores = nome.count(nome)
# # método de escrita em um arquivo csv
# # escrever = open('arquivos/intersecao.csv', 'w')
# # escrita = csv.writer(escrever)
# # escrita.writerow(["nome", "número", "email", "país", "estado", "renda"])
# # escrita.writerows(str(intersecao))
# # escrever.close()

print(nao_devedores)

print(nov_intersecao.count(nov_intersecao))
