#!/bin/bash
echo "Parâmetros digitados: $1 $2"

if [ $1 -gt $2 ]; then
    echo "Primeiro número digitado é o maior"
elif [ $2 -gt $1 ]; then
    echo "O Segundo número digitado é o maior"
else
    echo "Os números são iguais"
fi

echo "A soma dos números é: `expr $1 + $2`"
