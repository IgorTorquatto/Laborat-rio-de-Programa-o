nome = "lorenzo"
sobrenome = 'romão'
nome_completo = nome + " " + sobrenome

#Upper: (Transfoma todos os caracteres em maiúsculo)
print(nome_completo.upper())

#Lower: (Transfoma todos os caracteres em minúsculo)
print(nome_completo.lower())

#Strip: (Retira os espaços do início e do final de uma string)
espacos="  nome  "
print(espacos.strip())

#Caracteres especiais:
# \n Quebra Linha:
print("Meu nome é \n Romão")
# \t Tabulação:
print("\t Exemplo")
# \ Para printar aspas:
print("\"Texto com aspas\"")

#Lembrando que podemos definir que a variável receberá um dado tipo str:
variavel=str("Nome")
print(variavel)