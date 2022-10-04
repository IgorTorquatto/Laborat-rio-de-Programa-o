nome="Michael"
sobrenome="Corleone"
idade= 45

print("Meu nome é {} {} e tenho {} anos.".format(nome,sobrenome,idade))

#Podemos colocar identificações dentro das chaves e na formatação passar a relação desse nome com cada variável que queremos.
print("Meu nome é {um} {dois} e tenho {tres} anos.".format(um=nome,dois=sobrenome,tres=idade))

#Manipulando o valor float:
#Arredonda para cima e , no exemplo, usa somente uma casa decimal após o ponto flutuante:
dinheiro=576.39
print("Tenho R$ {valor:.1f}".format(valor=dinheiro))