#Algumas vezes, precisamos saber o que o parâmetro de uma função receberá , seja para usar métodos de tuplas,listas,dicts etc
#Ou para dar manuntenção em códigos de utros programadores.
#Portanto, quando passamos um parâmetro podemos dar uma dica do tipo que ela irá receber:
#Depois da flecha indica qual será o tipo do return.

def desconto(produtos: dict,desconto: float) -> (dict):
    resultado={}

    for nome_produto,valor in produtos.items():
        resultado[nome_produto]= f"{valor * (1 - desconto):.2f}"

    return resultado

dicionario= {
    "Microondas": 1500.15,
    "Geladeira": 2000.5,
    "Porta": 50.0
}

print(desconto(dicionario,0.15))

#Exemplo varáveis :

lista: list= "1,2,3,4,5".split(',')