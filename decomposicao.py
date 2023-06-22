import math
import sys

num = input("digite um número:")

try:
    num = int(num)
except:
    print("'{0}' não é um número! Por favor rode novamente".format(num))
    sys.exit(2)

digits = int(math.log10(num))+1
result = list()

def calc_num(num):
    x = num
    novas_dezenas = int(x / 10)
    num_new = x % novas_dezenas
    result.append(num_new)
    num = novas_dezenas
    return num


if digits == 2:
    left_algoritm = int(num / 10)
    result.append(left_algoritm)
    right_algoritm = num % 10
    result.append(right_algoritm)
    print(result)
else:

    while digits >= 3:
        # calculo
        #numero antigo
        num = calc_num(num)
        digits = int(math.log10(num))+1

    else:
        right_algoritm = num % 10
        result.append(right_algoritm)
        left_algoritm = int(num / 10)
        result.append(left_algoritm)

while result:
    print(result.pop())

