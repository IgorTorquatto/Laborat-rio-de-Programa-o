num1=input("Digite um número: ")
num2=input("Digite um número: ")

operacao=input("Digite a operação que você quer realizar: \n + para adição\n - para subtração\n  * para multiplicação\n / para divisão: \n")

equacao=f"{num1} {operacao} {num2}"

#Eval para converter a string recebidas pelos inputs:
resultado=eval(equacao)

string=" Resultado: "

print(f"{string:*^50}")
print("{}".format(resultado))