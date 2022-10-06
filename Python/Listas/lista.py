#Podemos acessar cada elemento através de índices e podemos armazenar nas listas diferentes tipos de dados
#Notação -> Colchetes
lista=[1,"nome",2.5,False]
print(f"Lista: {lista}")
print(f"Elemento da posição 2: {lista[2]}")
print("Elemento por elemento: ")
contador=0
while contador < len(lista):
    print(f"{lista[contador]}")
    contador+=1