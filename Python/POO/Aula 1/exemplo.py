from random import choice

#As classes servem como modelo para a criação de objetos que nós usaremos , posteriormente , no nosso código.

class Desenvolvedor:
    def __init__(self,linguagens_programacao=None):
        self.linguagens_programacao = linguagens_programacao
        print(f'Novo dev com experiência nas linguagens: {self.linguagens_programacao}')

    def desenvolver_codigo(self):
        print("Dev codando em {}")