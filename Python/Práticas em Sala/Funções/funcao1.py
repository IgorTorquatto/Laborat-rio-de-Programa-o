#Uma função em Python pode retornar dois valores
def velocidade_e_aceleracao(distancia,tempo):
    v= distancia/tempo
    a= v / tempo
    return v,a

print(f"Velocidade e Aceleração {velocidade_e_aceleracao(10,2)}")