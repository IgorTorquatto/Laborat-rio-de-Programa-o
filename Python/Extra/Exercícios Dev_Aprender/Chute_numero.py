#Crie um jogo que o usuário deve acertar um número aleatório gerado pelo sistema.
from random import randint


numero_magico=randint(0,10)
numero_usuario=input("Digite um número [0,10]: ")

if int(numero_usuario) == (numero_magico):
    print(f"Parabéns, você acertou o número {numero_magico} ;D !")
elif int(numero_usuario) !=(numero_magico):
    print(f"Você errou, o número certo era {numero_magico} :C .Tente Novamente.")
else:
    print("Opção Inválida. Tente Novamente.")


