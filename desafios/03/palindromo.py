# Crie um script que verifica se uma palavra ou frase fornecida pelo usuário é um palíndromo. 
# Palíndromo é uma palavra ou uma frase que de frente pra trás e de trás pra frente são iguais, 
# por exemplo, "ovo", "radar" e "Ame o poema".

palindromo = input("Escreva a palavra para verificar se é palíndromo: ")

palindromo = palindromo.lower()
palindromo = palindromo.replace(" ", "")
palindromo = palindromo.replace("!", "")
palindromo = palindromo.replace("?", "")
palindromo = palindromo.replace(".", "")
palindromo = palindromo.replace(",", "")

for i in range(len(palindromo) // 2):
    if palindromo[i] != palindromo[-(i + 1)]:
        print("A palavra não é um palíndromo.")
        break
else:
    print("A palavra é um palíndromo.")