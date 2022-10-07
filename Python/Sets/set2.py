#Métodos e Manipulação de Sets:
carteira={"Magalu","BMG","Ifood","Youtube"}
print(f"Carteira inicial: {carteira}")

#Add para adicionar elementos: (Lembrando que sets não permitem elementos duplicados)
carteira.add("Magalu")
print(f"Carteira após o add -> {carteira}")

#Update atualiza nosso set , adicionando mais de um elemento: (Update != add , deve estar no mesmo tipo de iterado que queremos adicionar seja set,tupla,lista ou dict)
carteira.update({"Magalu","MCdonalds"})
print(f"Carteira após o update -> {carteira}")

#Discard descarta o elemento passado:
carteira.discard("BMG")
print(f"Carteira após o discard -> {carteira}")

#Remove é igual o discard , porém caso passarmos para o remove remover um item que não existe ele gera erro e o discard não gera erro , o discard simplesmente não remove o item que não existe.

#Pop remove o último elemento, porém como o set não é ordenado ele sempre vai remover o último elemento e esse elemento sempre será um elemento aleatório:
carteira.pop()
print(f"Carteira após o pop -> {carteira}")

#Clear limpará todo o set:
carteira.clear()
print(f"Carteira após o clear -> {carteira}")
