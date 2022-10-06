#Fatiamento de Listas 
#lista[inicio:fim:passo] sendo o fim excludente, Logo:
#Se tivermos uma lista=[a,b,c,d,e,f] com indices de 0 a 5 e quisermos ter uma lista menor chamada de parte_1=[a,b,c] devemos:
#parte_1=lista[0:3:1]

letras=["a","b","c","d","e","f"]
parte_1=letras[0:3:1]
parte_2=letras[3:6:1] #Queremos d,e,f
print(parte_1)
print(parte_2)
print(parte_1+parte_2)

#Se ficar vazio [ : : ] o python vai do primeiro até o último índice.
letras_inversas=letras[::-1]
print(letras_inversas)
#Caminha do final até o início de um em um 