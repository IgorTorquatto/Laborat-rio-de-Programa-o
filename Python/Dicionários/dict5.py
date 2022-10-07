#Métodos dos dicionários.
familia={
    "pai": "José",
    "mãe": "Maria",
    "filho": "Antônio",
    "filha": "Francisca"
}

print(f"Família inicial: {familia}")

#Copy copia o mesmo dicionário, mas claro com referência diferente:
nova_familia=familia.copy()
print(f"Cópia família: {nova_familia}")

#Items retorna os pares chave e valor em formato de lista:
pares_lista=familia.items()
print(f"Pares do dicionário em Lista: {pares_lista}")

#Keys retorna todas as chaves em forma de lista
chaves=familia.keys()
print(f"Chaves: {chaves}")

#Values retorna todos os valores em forma de lista
valores=familia.values()
print(f"Valores: {valores}")

#Setdefault insere uma nova chave caso não exista (O valor deve ser passado dentro da função também) e , caso a chave já exista, retorna o valor.
familia.setdefault("sobrinho","Chico")
print(f"Família com adição: {familia}")
existente=familia.setdefault("pai")
print(f"Existente: {existente}")

#Fromkeys cria um dicionário a partir de chaves :
chaves=["pai","mãe","filho"]
valor=0
jogo=dict.fromkeys(chaves,valor)
print(f"Jogo: {jogo}")