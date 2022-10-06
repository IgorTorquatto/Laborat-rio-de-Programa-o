#Alguns métodos de Listas:
sacola=["Arroz","Feijão","Carne","Farinha"]
print(f"Lista Inicial: {sacola}")

#Append adicona itens ao final da lista:
sacola.append("Macarrão")
print(f"Lista após o append: {sacola}")

#Extend adiciona todos os itens de outra estrutura ao fim da lista:
sacola.extend(["Maionese","Ketchup"])
print(f"Lista após o extend: {sacola}")

#Insert inserir um elemento na posição desejada:  Formatação -> (indice,item desejado)
sacola.insert(0,"Milho")
print(f"Lista após o insert: {sacola}")

#Remove irá remover o PRIMEIRO elemento IGUAL ao valor passado:
sacola.remove("Macarrão")
print(f"Lista após o remove: {sacola}")

#Pop remove o item da posição desejada da lista e o remove, caso o índice não seja especificado, retorna o último elemento:
sacola.pop()
print(f"Lista após o pop remover o final: {sacola}")
sacola.pop(3)
print(f"Lista após o pop remover o elemento de índice 3: {sacola}")

#Index retorna o índice de um determinado valor:
indice=sacola.index("Farinha")
print(f"Usando o index para saber o índice do elemento farinha: {indice}")
#Podemos passar, além do valor , os índices de início e fim que queremos que seja feito a checagem
posicao=sacola.index("Milho",0,3)
print(f"Posição de milho: {posicao}")

#Count conta o número de ocorrências do valor especificado na lista:
ocorrencias=sacola.count("Arroz")
print(f"O número de vezes que a palavra Arroz aparece é: {ocorrencias}")

#Sort ordenada os itens da lista:
sacola.sort()
print(f"Lista ordenada com o sort: {sacola}")

#Reverse reverte a ordem original da nossa lista:
sacola.reverse()
print(f"Lista revertida com o reverse: {sacola}")

#Copy retorna uma lista com a cópia dos elementos da lista de origem
copia_sacola=sacola.copy()
print(f"Lista copiada com o copy: {copia_sacola}")

#Clear remove todos os elementos da lista:
sacola.clear()
print(f"Lista após o clear: {sacola}")