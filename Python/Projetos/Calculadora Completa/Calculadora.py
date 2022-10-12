#Funções
def soma(list):
    return int(list[0]) + int(list[1])

def subtracao(list):
    return int(list[0]) - int(list[1])

def multiplicacao(list):
    return int(list[0]) * int(list[1])

def divisao(list):
    return float(list[0]) / float(list[1])


#Programa:
if __name__ == "__main__":

    #O split é um método para strings que separa os elementos numa lista, sendo que nós determinamos onde será separado. Nesse caso, onde houver espaços:
    lista=input("Digite dois números separados por espaço: ").split(' ')
    if len(lista) != 2:
        while len(lista) !=2:
            lista=input("Informe apenas dois números separados por espaço: ").split(' ')
    
    operacao=input("\nDigite a operação a ser realizada: \n  \t + ) Adição \n \t - ) Subtração \n \t * ) Multiplicação \n \t / ) Divisão \n")

    if operacao in "+ - * /":
        if operacao == '+':
            print(f"Soma: {soma(lista)}")
        elif operacao == '-':
            print(f"Subtração:{subtracao(lista)}")
        elif operacao == '*':
            print(f"Multiplicação: {multiplicacao(lista)}")
        elif operacao == '/':
            print(f"Divisão: {divisao(lista)}")
    else:
        print("Foi informado uma operação inválida.")
