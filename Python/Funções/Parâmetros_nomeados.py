#Podemos atribuir nome aos argumentos quando formos passá-los, assim , sendo eles iguais aos dos parâmetos originais da função, podemos colocá-los em qualquer ordem;
def computador(cpu,memoria,hd):
    print(f"O computador tem como processador: {cpu}")
    print(f"O computador tem {memoria} GB de RAM")
    print(f"O computador tem {hd}GB")


computador(memoria=8,hd=500,cpu="i5")

#Parâmetros podem também ter valores padrão:
def computador2(cpu,memoria,hd,monitor=17):
    print(f"O computador tem como processador: {cpu}")
    print(f"O computador tem {memoria} GB de RAM")
    print(f"O computador tem {hd}GB")
    print(f"O monitor possui {monitor} polegadas")

computador2(memoria=8,hd=500,cpu="i5") # Se passarmos um valor diferente do padrão para monitor ele dá prioridade ao que passamos no argumento.
