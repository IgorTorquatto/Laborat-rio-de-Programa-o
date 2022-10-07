fila={
    "1": "Ana",
    "2": "Bosco",
    "3": "Carla",
    "4": "Dênis",
    "5": "Estefany"
}

print(f"Fila inicial: {fila}")

#Del deleta os elemenetos( Chave e valor ):
del fila['1']
print(f"Fila -1 pessoa: {fila}")

#Pop deleta o elemento da chave e retorna o elemento para ser posteriormente usado.
elemento=fila.pop('2')
print(f"Fila -1 pessoa: {fila}")
print(f"Elemento retirado: {elemento}")

#Popitem deleta o último item do dicionário:
fila.popitem()
print(f"Fila -1 pessoa: {fila}")

#Clear limpa o dicionário inteiro
fila.clear()
print(f"Fila vazia: {fila}")