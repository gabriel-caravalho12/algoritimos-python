import json
from decimal import Decimal, getcontext
import sys
import requests

value = input("digite o valor a ser convertido em reais:")

try:
    float(value)
except:
    print("'{0}' É Um Valor Não Valido!".format(value))
    print("Por Favor Digite Um Valor válido ...")
    sys.exit(2)

def resquest_data():
    url = requests.get('https://economia.awesomeapi.com.br/last/USD')
    dolar = json.loads(url.text)
    valor = dolar["USDBRL"]
    data = valor["high"]
    # print(type(data))
    return data

def calc_value(value):
    x = resquest_data()
    str(value)
    getcontext().prec = 4
    conversao = Decimal(x) * Decimal(value)
    return conversao

# a = calc_value("seu valor em reais é '{0}'".format(value))
a = calc_value(value)
print("o valor convertido será:R$ {0}".format(a))
