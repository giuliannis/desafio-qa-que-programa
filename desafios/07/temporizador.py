# Crie um programa que funcione como um temporizador (contagem progressiva) ou contador regressivo. 
# O usuário vai poder escolher entre as duas opções.

import time


modo = input("Escolha o modo 'progressivo' ou 'regressivo': ").lower()

tempo = input("Deseja definir o tempo desejado? (s/n): ").lower()

if tempo == "s":
    contagem = int(input("Digite o tempo em segundos: "))
else:
    contagem = 10

if modo == "progressivo":
    for i in range(contagem):
        print("Tempo decorrido: " + str(i + 1) + " segundos")
        time.sleep(1)
    print("Temporizador concluído!")

elif modo == "regressivo":
    for i in range(contagem, 0, -1):
        print("Tempo restante: " + str(i) + " segundos")
        time.sleep(1)
    print("Contador regressivo concluído!")

else:
    print("Modo inválido. Escolha 'progressivo' ou 'regressivo'.")