#!/bin/bash 
echo -n "Informe o nome do usuário a ser consultado: " 
read usuario 
pasta="/home/$usuario" 
if [ -d $pasta ];then 
    echo "O nome do usuário $usuario é válido no sistema." 
else 
    echo "O nome do usuário $usuario não é válido no sistema."
fi
