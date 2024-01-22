# Crie um programa que converta unidades de medida. 
# Para este desafio o foco são as conversões de Quilômetros para Milhas, 
# Milhas para Quilômetros, Metros para Pés, Pés para Metros, Graus Celsius para 
# Fahrenheit e Graus Fahrenheit para Celsius.


while True:
    valor = float(input("Escreva o valor a ser convertido: "))

    print("\nMenu de opções para conversão:")
    print("1. Quilômetros para Milhas")
    print("2. Milhas para Quilômetros")
    print("3. Metros para Pés")
    print("4. Pés para Metros")
    print("5. Graus Celsius para Fahrenheit")
    print("6. Graus Fahrenheit para Celsius")
    print("7. Finalizar")

    opcao = input("Escolha a opção para realizar a conversão: ")

    if opcao == "1":
        conversao = valor * 0.621371
        print("CONVERSÃO: \n" + str(valor) + " Quilômetros equivalem a " + str(conversao) + " Milhas")

    elif opcao == "2":
        conversao = valor * 1.60934
        print("CONVERSÃO: \n" + str(valor) + " Milhas equivalem a " + str(conversao) + " Quilômetros")

    elif opcao == "3":
        conversao = valor * 3.28084
        print("CONVERSÃO: \n" + str(valor) + " Metros equivalem a " + str(conversao) + " Pés")

    elif opcao == "4":
        conversao = valor * 0.3048
        print("CONVERSÃO: \n" + str(valor) + " Pés equivalem a " + str(conversao) + " Metros")

    elif opcao == "5":
        conversao = valor * 9/5 + 32
        print("CONVERSÃO: \n" + str(valor) + " Graus Celsius equivalem a " + str(conversao) + " Graus Fahrenheit")

    elif opcao == "6":
        conversao = (valor - 32) * 5/9
        print("CONVERSÃO: \n" + str(valor) + " Graus Fahrenheit equivalem a " + str(conversao) + " Graus Celsius")

    elif opcao == "7":
        print("Programa finalizado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
