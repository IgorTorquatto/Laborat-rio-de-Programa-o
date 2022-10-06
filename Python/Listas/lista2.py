from random import randint

alunos=['João','Clara','Felipe','Monica']

for i in alunos:
    nota=randint(0,10)
    print(f"A nota do(a) aluno(a) {i} foi {nota}.")

contador=0
while contador != len(alunos):
    contador+=1
print(f"Quantidade de alunos: {contador}")
