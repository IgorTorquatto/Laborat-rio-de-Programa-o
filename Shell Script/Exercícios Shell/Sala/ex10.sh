#!/bin/bash
i=0
while :
do
  echo -n "Digite uma palavra para incluir na lista: "
  read PALAVRA
  [ "$PALAVRA" == "sair" ] && break
  PALAVRAS[$i]="$PALAVRA"
  i=$((i+1))
  [ "${#PALAVRAS[@]}" -ge 2 ] && echo "${PALAVRAS[@]}" | tr ' ' '\n' | sort -d
done
