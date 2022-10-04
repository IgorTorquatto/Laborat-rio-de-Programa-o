#Strip para remover espaços:
variavel="  nome  "
print(variavel.strip())

#Upper para colocar as letras em maiúsculo:
variavel="grande"
print(variavel.upper())

#Lower para colocar letras para minúsculo:
variavel="PEQUENO"
print(variavel.lower())

#Replace para substituir um caractere por outro:
variavel="Tex,t,o Er,,rad,o"
print(variavel.replace(",",""))

#Count para contar quantas vezes aquele caractere foi contado dentro do nosso texto:
variavel="Quantos \"a's\" eu tenho?"
print(variavel)
print(variavel.count("a"))

#Center para centralizar nosso texto num número especificado de caracteres com o caractere de preenchimento escolhido:
variavel="Centralizado"
print(variavel.center(50,"*"))

#Index para ver a localização do primeiro caractere informado:
variavel="Onde está meu primeiro n?"
print(variavel)
print(variavel.index("n"))

#Isnumeric para testar se todos os caracteres da string são numéricos
variavel="Texto"
print(variavel.isnumeric())

#Slipt para Separar toda a string onde nós determinados e retornar uma lista de strings com "pedaços" da string original:
variavel="Texto grande para ser utilizado"
print(variavel.split(" ")) #Vai dividir onde tiver espaços.

#Title para colocar o primeiro caractere de cada palavra em maiúsculo:
variavel="Isto é um título"
print(variavel.title())

#Zfill para completar com 0's à esquerda a string que queremos até ficar com o número que determinamos:
variavel="588"
print(variavel.zfill(5))

#Len para verificar o tamanho da string
variavel="Esse é um exemplo de frase grande para que seja verificado o seu tamanho."
print(len(variavel))

#Encadeamento de Funções:
variavel="  T;e;x;;to  "
print(variavel.strip().replace(";","").upper().center(50,"-"))