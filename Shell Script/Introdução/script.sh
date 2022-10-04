echo Digite um número
 read num1
 echo Digite um número
 read num2
if [ $num1 -gt $num2 ]; then
    echo "Primeiro número digitado é o maior"
else
    echo "Segundo número digitado é o maior"
fi