#Classe é um Molde de Objetos:
#Utilizar primeira letra maiúscula, Não usar Underline:
class Celular:
    #Construtor:
    #Método que é chamado todas as vezes.
    #É dentro do construtor __init__ que se passa todos os atributos da nossa classe.
    #Podemos passar dicas , assim como nas funções, nos atributos:
    def __init__(self,fabricante: str,modelo: str,armazenamento,memoria,camera,bateria,tela_ligada: bool ):
       #Com o self criamos uma instância entre os atributos a serem passados.
       self.fabricante=fabricante
       self.modelo=modelo
       self.armazenamento=armazenamento
       self.memoria=memoria
       self.camera=camera
       self.bateria=bateria
       self.tela_ligada=tela_ligada


    def ligar_tela(self):
        #Usamos o self para mudar a variavel que queremos:
        self.tela_ligada = True


celular_android = Celular("Samsung","S10",6.25,128,4.21,3400,False)
#A passagem dos atributos não precisa ser posicional:
celular_iphone = Celular(fabricante="Apple",modelo="Iphone13",armazenamento=128,memoria=3,camera=16,bateria=2650,tela_ligada=False)

#Usar um método:
celular_iphone.ligar_tela()

print(celular_iphone.tela_ligada)
