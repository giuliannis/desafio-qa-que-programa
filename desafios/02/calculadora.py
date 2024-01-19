# Desenvolva um programa que realize operações básicas de matemática, como adição, subtração, multiplicação e divisão.

conta = input("Escreva a operação matemática: ")
primeiroValor, operacao, segundoValor = conta.split(" ")

primeiroValor = int(primeiroValor)
segundoValor = int(segundoValor)

if operacao == "+":
    print(primeiroValor+segundoValor)
    
elif operacao == "-":
    print(primeiroValor-segundoValor)
    
elif operacao == "*" or operacao == "x":
    print(primeiroValor*segundoValor)
    
elif operacao == "/":
    if segundoValor == 0:
        print("Não existe divisão por 0")
    else:
        print(primeiroValor/segundoValor)
    