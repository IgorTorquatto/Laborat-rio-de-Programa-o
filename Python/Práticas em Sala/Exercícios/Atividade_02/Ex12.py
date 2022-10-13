num_a=int(input("Digite um número a: "))
num_b=int(input("Digite um número b: "))

contador=0
for i in range (num_a,num_b):
    contador+=1

print(f"Existem {contador} números nesse intervalo.")
