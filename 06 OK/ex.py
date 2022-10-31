tupla = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# tupla = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

lista = list(tupla)

reserva = []
res = []

for element in lista:
    element = list(element)
    reserva.append(element)

var = 0

for element in reserva:
    for item in element:
        var += item
        # print(var)
    print(res)
    var = var / len(element)
    res.append(var)
    var = 0


# print(lista)
print(reserva)
print(res)

"""
O ALGORITMO ESTÁ CERTO, REVEJA O ENUNCIADO
"""