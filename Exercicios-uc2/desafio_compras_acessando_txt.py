'''
Esse desafio consiste em somar os itens de um lista de compras.

Site do desafio: https://jocile.com/Programador/Desafios/Desafio-total-de-compras
Criado a partir do desafio_compras em https://github.com/IllgnerPeixoto/Aula_py/

- [X] Organizar os códigos em funções
- [X] Criar uma função para salvar a lista e o total em um arquivo txt.
- [X] Criar uma nova opção no menu para salvar a lista.

Nova fase criando a lista de produtos (CRUD):
- [X] Criar uma lista de produtos e salvar em arquivo txt
- [X] Carregar a lista de produtos de um arquivo txt;
- [ ] Atualizar a lista adicionando novos produtos;
- [ ] Deletar um produto da lista

'''

produtos = {'Arroz': 5.90, 
            'Macarrão': 3.60,
            'Feijão': 8.50,
            'Carne': 50.90,
            'Frango':20.00,}

carrinho = []

def mostrar_produtos():
    print('Produtos Disponíveis:')
    for produto, valor in produtos.items():
        print(f"{produto}: R$ {valor}")

def adicionar_produto(total_compras):
    adicione = input("Digite o nome do produto: ")
    if adicione in produtos:
        carrinho.append(adicione) #adiciona o produto ao carrinho
        total_compras += produtos[adicione] #soma o valor dos produtos adicionados
        print(f'{adicione} adicionado ao carrinho. Total até o momento: R$ {total_compras}')
    else:
        print("Produto não encontrado. Tente novamente.")
    return carrinho, total_compras

def mostrar_menu():
    total_compras = 0.0
    menu = """
    Escolha uma opção dos produtos: 
    [m] Mostrar [a] Adicionar [c] Carrinho
    [s] salvar  [l] ler o carrinho de compras
    f -(Finalizar Compra)
    """
    while True:
        opcao = input(menu)
        if opcao == 'm':
            mostrar_produtos()
        elif opcao == 'a':
            carrinho, total_compras = adicionar_produto(total_compras)
        elif opcao == 'c':
            print("Produtos no carrinho:")
            for produto in carrinho:
                print(produto)
        elif opcao == 's':
            salvar_lista(carrinho, total_compras)
            print("Lista salva com sucesso!")
        elif opcao == 'l':
            carrinho, total_compras = carregar_lista()
            print("Lista carregada com sucesso!")
        elif opcao == 'f':
            print("\nProdutos escolhidos:", ', '.join(carrinho))      
            print(f"Total da compra: R$ {total_compras}")
            break

def salvar_lista(carrinho, total_compras):
    with open("Exercicios-uc2/lista_compras.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Produtos escolhidos: {', '.join(carrinho)}\n")
        arquivo.write(f"Total da compra: R$ {total_compras}")

def carregar_lista():
    try:
        with open("Exercicios-uc2/lista_compras.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            carrinho = linhas[0].split(": ")[1].split(", ")
            total_compras = float(linhas[1].split(": R$ ")[1])
            return carrinho, total_compras
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return [], 0.0
    except IOError:
        print("Erro ao ler o arquivo")
        return [], 0.0

mostrar_menu()