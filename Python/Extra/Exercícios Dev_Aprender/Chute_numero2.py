from random import randint

numero_magico=randint(0,10)
numero_usuario=input("Digite um número [0,10]: ")

while int(numero_usuario) != numero_magico:
    if int(numero_usuario) > numero_magico:
        numero_usuario=input("Você errou, tente novamente (Dica-> O número mágico é menor do que o digitado.): ")
    elif int(numero_usuario) < numero_magico:
        numero_usuario=input("Você errou, tente novamente (Dica -> O número mágico é maior do que o digitado.): ")

print(f"Parabéns, você acertou o número {numero_magico} ;D !")
