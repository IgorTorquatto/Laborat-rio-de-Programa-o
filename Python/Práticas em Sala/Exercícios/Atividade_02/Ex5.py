import math


def cria_vetor(list: list):
    for i in range(0,3):
        list.append(int(input(f"Digite um número para a posição {i+1} do vetor: ")))
    return list


def calcula_norma(list: list):
    soma_quadrados=0
    for i in range(0,len(list)):
        soma_quadrados= soma_quadrados + (int(list[i])**2)
    

lista_1=[]
lista_2=[]
lista_3=[]
print(f"\n Valores para a lista_1: ")
cria_vetor(lista_1)
print(f"\n Valores para a lista_2: ")
cria_vetor(lista_2)
print(f"\n Valores para a lista_3: ")
cria_vetor(lista_3)


