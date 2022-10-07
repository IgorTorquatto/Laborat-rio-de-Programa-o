computador={
    "cpu": "Ryzen3",
    "ram": "DDR4 4GB",
    "gpu": "RTX 1660",
    "hd": "250GB"
}

texto="Computador versão "
print(f"{texto} 1 {computador}")

#Alterando dicionário:
computador["ram"]="DDR4 8GB"
print(f"{texto} 2 {computador}")

#Adicinando no dicionário:
computador["fonte"]="500W"
print(f"{texto} 3 {computador}")

#Utilizando método update para atualizar várias informações ao mesmo tempo:
computador.update({"fonte": "650W","cpu":"Core i9","hd": "1TB"})
print(f"{texto} 4 {computador}")
