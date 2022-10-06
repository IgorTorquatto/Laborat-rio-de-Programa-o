lista=[1,2,3]

#Primeira variável não precisa ser declarada anteriormente, ela é apenas uma variável de iteração. 
#Segunda variável pode ser uma lista,tupla,dicionário ou range.
for i in lista:
    print(f"{i}")
#1,2,2
print("\n")
#Em C:
# for (i = 0; i<=10; i++)
#Em python: (Perceba que o parâmetro do meio deve ser sempre um a mais de onde nós realmente queremos chegar, o terceiro parâmetro é o passo e o primeiro é o início)
for i in range(0,11, 1):
    print("{}".format(i))
