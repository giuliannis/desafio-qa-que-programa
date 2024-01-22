# Desenvolva um script que gere e exiba uma lista com 6 números aleatórios entre 1 e 60, 
# sem repetições (ou seja, dentre os seis números selecionados, 
# não podem existir números repetidos), 
# para que você possa fazer um jogo da Mega Sena.

import random

lista = []

while len(lista) < 6:
    aleatorio = random.randint(1, 60)
    
    if aleatorio not in lista:
        lista.append(aleatorio)

print("Os números para Mega Sena são: " + str(lista))



