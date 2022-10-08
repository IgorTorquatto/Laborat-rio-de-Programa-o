def maior(num1,num2):
    if num1 > num2:
        print(f"O primeiro número({num1}) é o maior.")
    elif num2 > num1:
        print(f"O segundo número({num2}) é o maior.")
    else:
        print(f"Os números são iguais({num1})")



numero1=int(input("Digite um número: "))
numero2=int(input("Digite outro número: "))

maior(numero1,numero2)