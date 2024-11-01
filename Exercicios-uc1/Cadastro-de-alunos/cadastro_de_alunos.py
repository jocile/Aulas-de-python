'''
Criar um aplicativo em Python que funcione como um sistema de cadastro de alunos para uma escola.
O sistema deve permitir a inserção, consulta e exclusão de dados dos alunos.
'''


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
        # Buscar um aluno por matrícula e exibir seus dados completos.
        buscar_matricula = input("Digite a matrícula do aluno que deseja consultar: ")
        if buscar_matricula in alunos:
            aluno_encontrado = alunos[buscar_matricula]
            print(f"Aluno encontrado: {aluno_encontrado['nome']}")
            print(f"Matrícula: {buscar_matricula}")
        else :
            print("Aluno não encontrado!")
            
    elif opcao == "3":
        # TODO : Excluir Aluno
        pass
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")

print(alunos.items())
