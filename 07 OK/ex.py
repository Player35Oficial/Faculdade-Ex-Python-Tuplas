# tupla = (1,2,3)
tupla = (10, 20, 40, 5, 70)

lista = list(tupla)

reserva = []

aux = 0
filtro = 0

for item in lista:
    item = str(item)
    reserva.append(item)

reserva = int(reserva[0] + reserva[1] + reserva[2])
# tuple(filtro)
print(tupla)
print(reserva)