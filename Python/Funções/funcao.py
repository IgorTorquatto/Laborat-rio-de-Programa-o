# Quando se define uma função temos que usar a palavra def
# O nome da função
# O parâmetro é onde posteriormente deve ser passado um argumento, ou seja paramêtro != argumento
def diz_ola(nome):
    return f"Olá Mundo, meu nome é {nome}"

#Podemos passar o argumento sem especificar:
retorno=diz_ola("Igor")
print(retorno)

#Ou podemos especificar qual parâmetro recebe qual argumento:
retorno_2=diz_ola(nome="Pedro")
print(retorno_2)
