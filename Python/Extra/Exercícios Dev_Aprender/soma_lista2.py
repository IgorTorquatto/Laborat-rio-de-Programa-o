def soma_lista(list):
    auxiliar=0
    for i in range(0,len(list)):
        auxiliar=auxiliar+int(list[i])
    return auxiliar


lista =[]
#Lembrando que a função range é [ num , num )
for i in range(0,5):
   lista.append(int(input(f"Digite o valor para a posição {i+1} da lista. ")))
print(f"Soma total: {soma_lista(lista)}")