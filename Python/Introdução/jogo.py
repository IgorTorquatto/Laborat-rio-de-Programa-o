palavra_secreta='gnostico'
letras_acertadas=['_','_','_','_','_','_','_','_',]
print(letras_acertadas)

acertou=False 
enforcou=False
erros=0

while(not acertou and not enforcou):
    chute=input('Qual é a letra: ')
    if(chute in palavra_secreta):
        posicao=0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[posicao]= letra
                print(letras_acertadas)
            posicao+=1
    else:
        erros+=1
    enforcou= erros==6
    acertou='_' not in letras_acertadas

if(acertou):
    print("Parabéns!")
    print("Palavra secreta: "+ palavra_secreta)

if(enforcou):
    print("Deu ruim :( ")


