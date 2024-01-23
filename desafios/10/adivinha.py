# Desenvolva um jogo de adivinhação em que o usuário deve adivinhar um número gerado aleatoriamente pelo programa.

import random

def numero_aleatorio():
    return random.randint(1, 100)

def obter_tentativa():
    return int(input("Digite sua tentativa: "))

def fornecer_feedback(tentativa, numero_certo):
    if tentativa == numero_certo:
        print("Parabéns! Você acertou o número " + str(numero_certo) + " !")
        return True
    elif tentativa < numero_certo:
        print("O número é maior. Tente novamente.")
    else:
        print("O número é menor. Tente novamente.")
    return False

def jogar_rodada():
    numero_certo = numero_aleatorio()
    tentativas_restantes = 7

    print("Tente adivinhar um número entre 1 e 100.")
    print("Você tem 7 tentativas a cada rodada.")

    while tentativas_restantes > 0:
        tentativa = obter_tentativa()
        if fornecer_feedback(tentativa, numero_certo):
            return True

        tentativas_restantes -= 1
        print("Tentativas restantes: " + str(tentativas_restantes))

    print("Fim do jogo. O número correto era " + str(numero_certo) + ". Você não acertou desta vez.")
    return False

def main():
    pontuacao_total = 0

    while True:
        print("\nBem-vindo ao Jogo de Adivinhação!")
        print("\nEscolha uma das opções abaixo! ")
        print("1. Jogar")
        print("2. Ver Pontuação")
        print("3. Zerar Pontuação")
        print("4. Sair")

        opcao = input("Digite a opção escolhida: ")

        if opcao == "1":
            pontuacao_rodada = jogar_rodada()
            pontuacao_total += pontuacao_rodada
            pontuacao_rodada = int(pontuacao_rodada)
            print("Você ganhou " + str(pontuacao_rodada) + " pontos nesta rodada.")
        elif opcao == "2":
            print("Sua pontuação total: " + str(pontuacao_total))
        elif opcao == "3":
            pontuacao_total = 0
            print("Pontuação zerada com sucesso!")
        elif opcao == "4":
            print("Saindo do jogo. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
