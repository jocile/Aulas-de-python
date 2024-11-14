'''
 Sistema de Cadastro de Alunos
 Esse sistema deve permitir a inserção, consulta, atualização e exclusão de dados dos alunos.
https://jocile.com/Programador/Desafios/cadastro+de+alunos/Desafio+cadastro+de+alunos
'''

def main():
    while True:
        print("\nMenu Principal:")
        print("1. Cadastrar Aluno")
        print("2. Consultar Aluno")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            consultar_aluno()
        elif opcao == "3":
            atualizar_aluno()            
        elif opcao == "5":
            excluir_aluno()
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

def cadastrar_aluno():
    # Implementar a funcionalidade de cadastro de aluno
    pass

def consultar_aluno():
    # Implementar a funcionalidade de consulta de aluno
    pass

def atualizar_aluno():
  # Implementar a funcionalidade de atualização de aluno
    pass

def excluir_aluno():
    # Implementar a funcionalidade de exclusão de aluno
    pass

if __name__ == "__main__":
    main()