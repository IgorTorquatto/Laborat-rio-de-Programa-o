def media(list):
    soma=sum(list)
    media= soma / len(list)
    return media

def maior(list):
    maior=0
    for i in list:
        if i > maior:
            maior=i
    return maior

def menor(list):
    menor=min(list)
    return menor

def positivos(list):
    contador=0
    for i in list:
        if i >=0:
            contador+=1
    return contador

def negativos(list):
    contador=0
    for i in list:
        if i < 0:
            contador+=1
    return contador


lista= []
for i in range(0,10):
    lista.append(float(input(f"Digite um número para a posição {i+1} da lista: ")))

print(f"A média dos valores digitados na lista é de: {media(lista)}")
print(f"O maior valor da lista é o número: {maior(lista)}")
print(f"O menor valor da lista é o número: {menor(lista)}")
print(f"Quantidade de números positivos: {positivos(lista)}")
print(f"Quantidade de números negativos: {negativos(lista)}")