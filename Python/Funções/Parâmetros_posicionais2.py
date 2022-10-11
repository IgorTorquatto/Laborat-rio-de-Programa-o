#Tendo em vista isso, vamos fazer um somador que possamos , posteriormente, atribuir vários argumentos:
def soma(*numeros):
    resultado=0
    for numero in numeros:
        resultado+=numero
    return resultado


print(f"Soma total: {soma(1,2,3,4,5,6,7,8,9)}")
