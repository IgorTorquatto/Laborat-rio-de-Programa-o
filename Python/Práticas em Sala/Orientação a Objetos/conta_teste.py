from conta import Conta

conta=Conta('123-4','João',120.0,1000.0)

print(conta.numero)
print(conta.titular)

conta.deposita(50.0)
conta.extrato()
conta.saca(20.0)
conta.extrato()
