matriz = [
    [1, 2, 3, 5],
    [4, 5, 6, 7],
    [7, 8, 9, 9],
    [9, 1, 4, 3],
]

indx = 0
x = matriz[0]

# for y in matriz:
#     while indx < limit:
#         print(type(y))
#         indx += 1
#     print(x.index(range(0, limit)))

print("o tipo de matriz é:{0}".format(type(matriz)))
print("o tipo de x é:{0}".format(type(x)))

while len(matriz) == len(x):
    """
    enquanto o meu x e y forem iguais imprima o y
    """
    y = x[indx]
    print(y)
    indx += 1
    x = matriz[indx]
    print(x)