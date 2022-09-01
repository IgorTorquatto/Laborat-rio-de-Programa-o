#!/bin/bash
#Preferi fazer um menu

main() {
echo "Digite o número da operação:"
echo
echo "1. Soma [+]"
echo "2. Subtração [-]"
echo "3. Multiplicação [×]"
echo "4. Divisão [÷]"
echo "5. Sair"
echo
read opcao 
case $opcao in
  1) soma ;;
  2) subt ;;
  3) multi ;;
  4) divi ;;
  5) sair ;;
esac
}

soma() {
  echo -n "Digite um número:" 
  read valor1
  echo -n "Digite outro número:"
  read valor2
  echo "Calculando..."
  soma=$((valor1+valor2)) 
  echo "$valor1 + $valor2 = $soma"
}

subt() {
  echo -n "Digite um número:"
  read valor1
  echo -n "Digite outro número:"
  read valor2
  echo "Calculando..."
  subtr=$((valor1-valor2))
  echo "$valor1 - $valor2 = $subtr"
}

multi() {
  echo -n "Digite um valor:"
  read valor1
  echo -n "Digite outro valor:"
  read valor2
  echo "Calculando..."
  mtp=$((valor1*valor2))
  echo "$valor1 × $valor2 = $mtp"
}

divi() {
  echo -n "Digite um valor:"
  read valor1
  echo -n "Digite outro valor:"
  read valor2
  echo "Calculando..."
  divisao=$((valor1/valor2))
  echo "$valor1 ÷ $valor2 = $divisao"
}

sair() {
 clear
 exit
}

#Chamada da função para dar funcionamento a tudo:
main