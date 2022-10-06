from random import randint

alunos=['João','Marcos','Felipe','José']
notas=[randint(0,10),randint(0,10),randint(0,10),randint(0,10)]

#Percorrer duas listas ao mesmo tempo:
#Sempre considera o tamanho da lista menor para igualar, em caso de listas diferentes.
for i,j in zip(alunos,notas):
    print(f"A nota do aluno {i.upper()} foi {j}.")
