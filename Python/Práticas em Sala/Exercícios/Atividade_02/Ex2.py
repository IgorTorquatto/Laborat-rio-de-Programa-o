lista= []
for i in range(0,10):
    lista.append(int(input(f"Digite um número para a posição {i+1} da lista: ")))
    
numero=int(input("Agora digite um número: "))

if numero in lista:
    print(f"O número {numero} existe na Lista.")
else:
    print(f"O número {numero} está na lista.")