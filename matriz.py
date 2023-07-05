matriz = [
    [1, 2, 3, 5],
    [4, 5, 6, 7],
    [7, 8, 9, 9],
    [9, 1, 4, 3],
]
"""
variáveis para melhor entender o que está acontecendo :)
"""
indx = 0
x = matriz[0]
limit = len(matriz) -1

print("o tipo de matriz é:{0}".format(type(matriz)))
print("o tipo de x é:{0}".format(type(x)))

"""
a diagonal principal em si
"""

while len(matriz) == len(x):
    """
    enquanto o meu x e y forem iguais imprima o y
    """
    y = x[indx]
    indx += range(1, limit)
    x = matriz[indx]
    print("o elemento de y é {0}".format(y))
