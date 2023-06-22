from decimal import Decimal
import sys

value = input("digite o valor a ser convertido:")

try:
    float(value)
except:
    print("'{0}' É Um Valor Não Valido!".format(value))
    print("Por Favor Digite Um Valor válido ...")
    sys.exit(2)

def calc_value(value):
    pass

a = calc_value(value)
print(a)