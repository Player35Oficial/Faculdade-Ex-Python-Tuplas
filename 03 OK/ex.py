listaTuplas = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

filtro = filter(None, listaTuplas)

listaTuplas = list(filtro)

print(listaTuplas)