idade=input("Digite sua idade: ")
sexo=input("Digite seu sexo [M/F]: ")

if sexo.upper() == "M":
    if int(idade) >= 65:
        print("Aposentadoria concedida.")
    else:
        print("Aposentadoria não concedida. Aguarde {} anos".format(65-int(idade)))

elif sexo.upper() == "F":
    if int(idade) >=60:
        print("Aposentadoria concedida.")
    else:
        print("Aposentadoria não concedida. Aguarde {} anos.".format(60-int(idade)))
else:
    print("Opção Inválida. Tente Novamente.")
