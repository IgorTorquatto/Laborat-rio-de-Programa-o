def pares(list):
    contador=0
    for i in list:
        if i % 2 == 0:
            contador+=1
    return contador


lista=[]
for i in range(0,10):
    lista.append(int(input(f"Digite um número para a posição {i+1} da lista: ")))

print(f"A lista que você digitou: {lista}")
print(f"Total de pares: {pares(lista)}")
