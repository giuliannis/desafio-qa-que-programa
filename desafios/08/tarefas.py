# Desenvolva uma aplicação simples para gerenciar uma lista de tarefas, permitindo adicionar e remover itens.

lista = []

while True:
    print("\nBem vindo! Escolha uma entre as opções abaixo")
    print("1. Adicionar uma tarefa")
    print("2. Remover uma tarefa")
    print("3. Listar todas as tarefas")
    print("4. Finalizar")

    escolha = input("Digite a opção escolhida: ")

    if escolha == "1":
        adicionar = input("Digite a nova tarefa: ")
        lista.append(adicionar)
        print("Tarefa adicionada com sucesso.")

    elif escolha == "2":
        if lista:
            remover = input("Digite a tarefa a ser removida: ")
            if remover in lista:
                lista.remove(remover)
                print("Tarefa removida com sucesso.")
            else:
                print("A tarefa não existe na lista.")
        else:
            print("A lista de tarefas está vazia. Não há tarefas para remover.")

    elif escolha == "3":
        if lista:
            print("Aqui estão as suas tarefas adicionadas: ")
            for index, tarefa in enumerate(lista, start=1):
                print(f"{index}. {tarefa}")
        else:
            print("A lista de tarefas está vazia.")

    elif escolha == "4":
        print("Saindo do Gerenciador de Tarefas. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
