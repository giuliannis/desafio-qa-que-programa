# Desenvolva um script que verifique se uma string fornecida pelo usuário é um e-mail válido.

import re

email = input("Digite um endereço de e-mail: ")

email = email.strip()
regular = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(regular, email):
    print("O e-mail é válido!")
else:
    print("O e-mail é inválido.")
