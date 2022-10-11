#A cada 1 cigarro fumado , -10minutos de vida.
def calculo(cigarros,anos):
    total_dias=anos * 365
    total_cigarros=cigarros * total_dias
    total_minutos=total_cigarros*10
    total_horas=total_minutos / 60
    total_diass=total_horas / 24
    print(f"Você fumou um total de {total_horas} horas , ou seja, se a cada 1 cigarro se perde 10 minutos de vida, você perdeu {total_diass:.2f} dias da sua vida. ")

    
cig_dia=int(int(input("Quantos cigarros você fuma por dia? ")))
periodo=int(input("Por quantos anos você já fumou/fuma? "))
calculo(cig_dia,periodo)