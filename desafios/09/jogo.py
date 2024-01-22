# Desenvolva um jogo que gera aleatoriamente um número e o jogador deve determinar 
# se esse número é primo ou não. O jogador ganha pontos por cada resposta correta.

import random

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

pontuacao = 0

while True:
    print("\nBem vindo ao Jogo de Números Primos!")
    print("1. Jogar")
    print("2. Ver Pontuação")
    print("3. Zerar Pontuação")
    print("4. Sair")

    escolha_menu = input("Escolha uma opção: ")

    if escolha_menu == "1":
        numero_aleatorio = random.randint(1, 100)
        print("Número atual: " + str(numero_aleatorio))
        resposta = input("É primo? (s/n): ").lower()

        if (resposta == "s" and primo(numero_aleatorio)) or (resposta == "n" and not primo(numero_aleatorio)):
            print("Resposta correta! +1 ponto")
            pontuacao += 1
        else:
            print("Resposta incorreta. O jogo acabou.")

    elif escolha_menu == "2":
        print("Sua pontuação atual: " + str(pontuacao))

    elif escolha_menu == "3":
        pontuacao = 0
        print("Pontuação zerada com sucesso!")

    elif escolha_menu == "4":
        print("Saindo do jogo. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
