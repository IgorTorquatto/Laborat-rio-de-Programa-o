def fatorial(num):
    contador=1
    valor=1
    while contador <= num:
        valor= valor * contador
        contador+=1
    return valor


numero=int(input("Digite um número: "))
print(f"Fatorial de {numero} é {fatorial(numero)}.")


