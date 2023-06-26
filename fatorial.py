import sys

entrada = input("digite um número inteiro para ser fatorado:")

try:
    valor = int(entrada)
except:
    print(" '{0}' é um valor inválido!".format(entrada))
    sys.exit(2)



while valor >= 0:
    for x in range(1, valor+1):
        aux = 1
        if x >= 1:
            aux += aux *(valor - 1)
            valor -= 1
        print(valor)
else:
    print("acabou!")