#!/bin/bash

echo -n "Caminho do diretório: "
read diretorio

ls -l $diretorio | while read linha; do
    if [ ${linha:0:1} = "d" ]; then
        echo $linha | awk '{print $9 " (dir)"}'
    else
        echo $linha  | awk '{print $9}'
    fi
done