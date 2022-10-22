#Nome da classe -> Maiúsculo

#Exemplo Sistema Bancário:

class Conta:
    
    #Métodos (Atributos):
    def __init__(self,id,nome,saldo):
        self.id= id
        self.nome= nome
        self.saldo= saldo
        
    
    def imprimir_nome(self):
        print(f"{self.nome}")
        
    
    def imprimir_saldo(self):
        print(f"{self.saldo}")
    
    
    def depositar(self,dinheiro):
        self.saldo=self.saldo + dinheiro
   
    

contauser1=Conta(1,"Jorge",10)
contauser2=Conta(2,"Paulo",20)

contauser2.imprimir_nome()
contauser2.imprimir_saldo()
contauser2.depositar(10)
print(f"Aumentado +10 na conta do usuário2: ")
contauser2.imprimir_saldo()
