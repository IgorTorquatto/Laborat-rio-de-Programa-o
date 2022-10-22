import math


def cria_vetor(list: list):
    for i in range(0,2):
        list.append(int(input(f"Digite um número para a posição {i+1} do vetor: ")))
    return list


def calcula_norma(list: list):
    soma_quadrados=0
    for i in range(0,len(list)):
        soma_quadrados= soma_quadrados + (int(list[i])**2)
    return math.sqrt(soma_quadrados)


#def maior(num1,num2,num3):
    
    

lista_1=[]
lista_2=[]
lista_3=[]
print(f"\n Valores para a lista_1: ")
cria_vetor(lista_1)
print(f"\n Valores para a lista_2: ")
cria_vetor(lista_2)
print(f"\n Valores para a lista_3: ")
cria_vetor(lista_3)

print("\n")

norma_1=calcula_norma(lista_1)
norma_2=calcula_norma(lista_2)
norma_3=calcula_norma(lista_3)
soma_normas= norma_1 + (norma_2+norma_3)

print(f"Norma do vetor_1: {norma_1}")
print(f"Norma do vetor_2: {norma_2}")
print(f"Norma do vetor_3: {norma_3}")


print(f"Soma das normas de todos os vetores: {soma_normas}")
