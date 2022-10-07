#Podemos passar um número infinito de parâmetros como no exemplo:
def numeros(arg1,arg2,*args):
    print(f"{arg1}")
    print(f"{arg2}")
    print(f"{args}")

if __name__ == '__main__':
    numeros(1,2,3,4,5)
#Args receberia 3,4,5.
