#Python não possui o comando switch, a maneira mais comum de fazer um código similar é usando if-else.
num=input("Digite um número: ")

if int(num) == 1:
    print("Um")
    pass
elif int(num) == 2:
    print("Dois")
    pass
elif int(num) == 3:
    print("Três")
    pass
else:
    print("Número não é nem 1,nem 2 e nem 3.")