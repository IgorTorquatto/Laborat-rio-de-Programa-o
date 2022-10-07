#Ordenada, permite valores duplicados, permite dados indexados, permite dados heterogêneos, 
#Notação ente parênteses
#Não podemos alterar valores em tuplas

tupla=(1,2,3,4,5,6,7,8,9)
print(tupla)

#Indexação:
print(f"O quinto elemento da tupla é {tupla[4]}")

#Slicing divide a tupla nos indices determinados:
dividido=tupla[4:]
print(f"Tupla do índice 4 a diante: {dividido}")

#Del -> não podemos deletar um valor de um índice pois tuplas não aceitam modificações, porém podemos deletar nossa tupla inteira:
del tupla

#Count -> mostra a quantidade de elementos que existem de acordo com o elemento que queremos que seja feita a checagem:
tupla=(1,2,3,4,5,6,7,8,9)
print(f"A quantidade de elementos iguais a 1 é {tupla.count(1)}")

#Index informa a posição do elemento:
print(f"O elemento 6 está na posição: {tupla.index(6)}")