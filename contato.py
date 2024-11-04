agenda = {"João": "123456789", "Maria": "987654321", "Pedro": "555555555", "Ana Rita": "44444444444"}

while True:
    print("\n-----🌟Agenda de Contatos🌟-----")
    print("1. Adicionar contato ➕")
    print("2. Remover contato 🗑️")
    print("3. Exibir contatos 👥")
    print("4. Sair 🔸")

    opcao = input("Escolha uma opção: ")
    print(50 * '-')

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        agenda[nome] = telefone
        print("Contato adicionado com sucesso!✅")
    elif opcao == "2":
        nome = input("Digite o nome do contato para remover 🗑️: ")
        if nome in agenda:
            del agenda[nome]
            print("Contato removido com sucesso!✅")
        else:
            print("Contato não encontrado na agenda. Tente novamente.")
    elif opcao == "3":
        print("Lista de contatos:")
        for nome, telefone in agenda.items():
            print("{}: {}📞".format(nome,telefone))
    elif opcao == "4":
        print("Encerrando...Até mais👋")
        break
    else:
        print("Opção inválida. Tente novamente.")