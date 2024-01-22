# Desenvolva um programa que conte o número de palavras em um texto fornecido pelo usuário. 
# O programa deve ser capaz de separar as palavras em um texto e determinar quantas palavras estão presentes.

palavras = input("Insira o texto: ")

palavras = palavras.split()
total = len(palavras)
print("O texto tem " + str(total) + " palavras")
    