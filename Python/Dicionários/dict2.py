dicionario={
    "id": "1",
    "nome": "Pedro",
    "filhos": ["Joana","Sara"],
    "compras":[
        {
            "id": 4.5,
            "produto": "Pc Gamer"
        }
    ]
}
#Como usamos as aspas duplas para passar a chave do objeto, nas f-strings temos que escolher entre aspas simples ou duplas para diferenciar da chave do objeto:
print(f"Acessando o primeiro elemento do array: {dicionario['compras'][0]}")
print(f"O usuário {dicionario['nome']} de id {dicionario['id']} comprou um {dicionario['compras'][0]['produto']} que tinha id {dicionario['compras'][0]['id']}.")

buscador=dicionario.get("filhos")
print(f"utilizando o método get para buscar uma chave: {buscador}")