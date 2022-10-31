# listaDeTuplas = [(1, 2), (2, 3), (3, 4)]
listaDeTuplas = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]

soma = []

for item in listaDeTuplas:
    item = list(item)
    soma.append(item)

res = []
for item in soma:
    var = 0
    for numero in item:
        var += numero
    res.append(var)

print(soma)

print(res)