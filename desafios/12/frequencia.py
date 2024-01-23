# Desenvolva um programa que analise a frequência de cada letra em um texto fornecido pelo usuário.

texto = input("Digite um texto: ")

letras = [letra.lower() for letra in texto if letra.isalpha()]

frequencia = {}
for letra in letras:
    frequencia[letra] = frequencia.get(letra, 0) + 1


print("\nTexto fornecido: " + str(texto))
print("Frequência de letras:")
for letra in letras:
    if frequencia[letra] > 0:
        print(str(letra) + ": " + str(frequencia[letra]))
        frequencia[letra] = 0
