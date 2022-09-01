#!/bin/bash
echo -n "Digite o nome do arquivo: "
read arquivo
consulta=$(sudo find /home/ -iname $arquivo)
if [ -e "$consulta"  ]; then
    echo "Encontrado em: $consulta"
    echo "Tamanho : $(ls -l $consulta | awk '{print $5}')  "
else
    echo "Não encontrado"
fi