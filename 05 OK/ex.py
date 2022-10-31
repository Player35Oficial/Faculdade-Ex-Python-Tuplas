tuplaOriginal = (4, 3, 2, 2, -1, 18)

tuplaNova = list(tuplaOriginal)

produto = 1

for elemento in tuplaNova:
    produto *= elemento

tuplaNova = tuple(tuplaOriginal)

print(tuplaNova)

print(f'Saída esperada: {produto}')
