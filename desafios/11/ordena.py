# Desenvolva um script que ordene uma lista de números fornecida pelo usuário.

lista = []


while True:
    entrada = input("Insira um número ou 'fim' para encerrar: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        lista.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

if lista:
    print("\nLista original: " + str(lista))
    print("Lista ordenada: " + str(sorted(lista)))
else:
    print("Nenhum número foi inserido. Nada a ordenar.")
