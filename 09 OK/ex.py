# listaDeTuplas = [(1, 2), (2, 3), (3, 4)]
listaDeTuplas = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
novaListaDeTuplas = []

for item in listaDeTuplas:
    item = list(item)


    novaListaDeTuplas.append(item)
    print(item)

print(novaListaDeTuplas)