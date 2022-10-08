#Crie um programa que receba o nome de um usário e dê boas vindas.
def bemvindo(nome):
    print(f"Bem-vindo(a) {nome.capitalize()} !")


usuario=input("Digite seu nome: ")
bemvindo(usuario)
