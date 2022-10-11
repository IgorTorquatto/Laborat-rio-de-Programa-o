lista=[]
for i in range (0,15):
    lista.append(float(input(f"Digite um número para a posição {i+1} da lista.")))

codigo=int(input("Digite um código: \n \t 0)Fechar o programa \n \t 1)Mostar a lista na ordem direta. \n \t 2)Mostrar a lista na ordem inversa."))

if codigo == 0:
    exit
if codigo == 1:
    print(f"Lista na ordem direta: {lista}")

if codigo == 2:
    print(f"Lista na ordem inversa: {lista.reverse()}")
