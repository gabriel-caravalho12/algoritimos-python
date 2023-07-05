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

"""
a diagonal principal em si
"""

while indx <= limit:
    """
    enquanto o meu x e y forem iguais imprima o y
    """
    y = x[indx]
    try:
        if indx == limit:
            print("{0}".format(y))
        else:
            pass
        indx += 1
        x = matriz[indx]
        print("{0}".format(y))



    except:
        print("processo finalizado!")


