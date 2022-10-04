#A função input serve para a entrada de dados.
#Por padrão, a função input recebe algo e já converte para o tipo string:
variavel=input("Digite um número para teste: ")
print(type(variavel))

numero=input("Informe um número: ")
print(f"O número digitado foi: {str(numero)}")

#Caso o usuário digite algo que não seja um dado tipo int dará erro:
numero2=int(input("Digite um número inteiro: "))
print(numero2)