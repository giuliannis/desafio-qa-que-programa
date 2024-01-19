# Desenvolva um programa que peça ao usuário para inserir um número. 
# O programa deve então verificar se o número é par ou ímpar e exibir uma mensagem informando o usuário.

valor = input("Digite um valor para saber se é par ou ímpar: ")
 
valor = int(valor)

if valor%2.0 == 0:
    print("O valor informado é par!")

else:
    print("O valor informado é ímpar!")