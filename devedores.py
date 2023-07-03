import csv


def search_cli():
    with open("arquivos/todos-os-clientes.csv") as csv_file:
        searchcliname = set()
        searchclicountry = set()
        clientes = csv.reader(csv_file, delimiter=",", quotechar='"')
        clientes = list(clientes)
        lencli = len(clientes)
        ind = 0
        while lencli and ind <= 500 - 1:
            linha = clientes[ind]
            nome = linha[0]
            country = linha[3]
            lencli -= 1
            ind += 1
            searchcliname.add(nome)
            searchclicountry.add(country)
    return searchcliname, searchclicountry

def search_dev():
    with open("arquivos/devedores.csv") as csv_file:
        searchdev = set()
        devedores = csv.reader(csv_file, delimiter=",", quotechar='"')
        devedores = list(devedores)
        lendev = len(devedores)
        ind = 0
        while lendev and ind <= 500 - 1:
            linha = devedores[ind]
            nome = linha[0]
            lendev -= 1
            ind += 1
            searchdev.add(nome)
    return searchdev


nomecli, countrycli = search_cli()
nomedev = search_dev()
dev = len(nomedev)

country = set()
intersection = set()

intersection = nomecli - nomedev
no_dev = len(intersection)
country = countrycli

print('o total de não devedores é:{0}'.format(no_dev))
print('seus nomes são: {0}'.format(intersection))
print('seus respectivos países são:{0}'.format(country))

print(no_dev)

# real
todos = len(nomecli)
real = dev + no_dev # devedores sao "315" e os não devedores sao "265"

print('prova real dos devedores:{0}'.format(real))
