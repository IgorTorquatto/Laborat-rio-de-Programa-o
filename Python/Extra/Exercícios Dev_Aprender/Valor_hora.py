#Retornar o valor/hora de um funcionário:
def valor_hora(salario,horas):
    valor= salario / horas
    return print(f"Você custa {valor:.2f}R$ por hora para a empresa. ")


sal=input("Digite o valor do seu salário: ")
hr=input("Quantas horas você trabalha por mês? ")
valor_hora(int(sal),int(hr))