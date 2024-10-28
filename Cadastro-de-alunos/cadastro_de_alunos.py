
alunos = {}
while True:
    print("\nMenu Principal:")
    print("1. Cadastrar Aluno")
    print("2. Consultar Aluno")
    print("3. Excluir Aluno")
    print("4. Sair")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        # Cadastrar aluno: Permitir a inserção de dados do aluno, incluindo nome, matrícula, curso e data de nascimento.
        aluno = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        curso = input("Digite o curso do aluno: ")
        data_nascimento = input("Digite a data de nascimento do aluno (dd/mm/yyyy): ")
        print(f"Aluno {aluno} cadastrado com sucesso!")
        alunos[matricula] = {"nome": aluno, "curso": curso, "data_nascimento": data_nascimento}
        
    elif opcao == "2":
        # TODO : Consultar Aluno
        pass
    elif opcao == "3":
        # TODO : Excluir Aluno
        pass
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")

print(alunos.items())
