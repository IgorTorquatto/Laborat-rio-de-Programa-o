from random import randint

Capacidade_máxima=1000
balde=0

while (balde<=Capacidade_máxima):
    volume_incrementado=randint(90,100)
    print(f"Foi incrementado {volume_incrementado}ml ao balde.")
    balde=balde+volume_incrementado
    print(f"O balde está com {balde}ml.\n")

if(balde > Capacidade_máxima):
    print(f"A sobra foi de {balde - Capacidade_máxima}")
else:
    print("O balde tem 1000ml")