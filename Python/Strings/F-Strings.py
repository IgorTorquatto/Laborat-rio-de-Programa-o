produto = "Televisor"
tamanho = 50
preco = 2299.99

print(f"Comprei um {produto} de tamanho {tamanho} polegadas.")

#Podemos organizar o conteúdo do print dentro da função e utilizando as f-strings:
print(
    f"Comprei um {produto.upper} \n"
    f"De tamanho {tamanho} \n"
    f"Que custou {preco}"
)

# ^ -> Centralizado.
# Numero do final-> Tamanho total de caracteres da string (Já contando com a que nós passamos).
# > -> alinhar à direita.
# < -> alinhar à esquerda.
# : -> quer dizer que a string será manipulada.
#Caractere após os : -> o caractere de preenchimento.
titulo= "Titulo"
print(f"{titulo:*^50}")