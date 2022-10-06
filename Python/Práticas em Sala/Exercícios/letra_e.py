lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]
mediaElementos = 0
for index in range(0, len(lista)):
#... seu código aqui
#Media de elementos
    mediaElementos =+ mediaElementos + lista[index]
    mediaElementos = mediaElementos / len(lista)
print(mediaElementos)