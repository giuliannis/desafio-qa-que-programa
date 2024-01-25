# Desenvolva um programa que seja capaz de gerar senhas aleatórias com critérios especificados pelo usuário, como comprimento e inclusão de números, letras maiúsculas, letras minúsculas e caracteres especiais.

import random
import string


comprimento = int(input("Bem vindo ao gerador de senhas! Informe o comprimento da senha desejada: "))
numeros = input("Deseja incluir números? (S/N): ").upper() == 'S'
letras_maiusculas = input("Deseja incluir letras maiúsculas? (S/N): ").upper() == 'S'
letras_minusculas = input("Deseja incluir letras minúsculas? (S/N): ").upper() == 'S'
caracteres_especiais = input("Deseja incluir caracteres especiais? (S/N): ").upper() == 'S'

caracteres = "".join(filter(None, [
    string.digits if numeros else "",
    string.ascii_uppercase if letras_maiusculas else "",
    string.ascii_lowercase if letras_minusculas else "",
    string.punctuation if caracteres_especiais else ""
]))

if not caracteres:
    print("Erro: Nenhum critério selecionado para gerar a senha.")
else:
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    print("\nSenha gerada:", senha)
