#Dado os valores de uma lista imprima sua soma:
def soma(lista):
    valor=sum(lista)
    return valor


list=[]
for i in range(0,5):
    list.append(int(input(f"Digite um valor para a posição {i+1} da lista: ")))

print(f"A soma de todos os valores da lista é: {soma(list)}")