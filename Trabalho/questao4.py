# INICIANDO O CONTADOR DE ID
contador_id = 1

# INICIANDO LISTA PARA ARMAZENAR LIVROS
livros = []

# VARIÁVEL PARA CONTROLAR SE A MENSAGEM DE BOAS-VINDAS JÁ FOI EXIBIDA
boas_vindas_exibida = False

# IMPRIMINDO MENU
def imprimir_menu():
    print(
        '******************************************\n'
        '--------------Menu Principal------------\n'
        '\n'
        '1 - Cadastrar Livros\n'
        '2 - Consultar Livro(s)\n'
        '3 - Remover Livro\n'
        '4 - Sair\n\n'
        '******************************************\n'
    )

# CADASTRANDO LIVRO
def cadastrar_livro():
    global contador_id

    nome_livro = input("Por favor entre com o nome do livro: ")
    nome_autor = input("Por favor entre com o nome do autor: ")
    nome_editora = input("E agora o nome da editora: ")

    livro = {
        'ID': contador_id,
        'nome_livro': nome_livro,
        'nome_autor': nome_autor,
        'nome_editora': nome_editora
    }

    livros.append(livro)
    
    print('*******************************************\n')
    print(f"Livro numero {contador_id} cadastrado com sucesso!\n\n Nome -> {nome_livro}\n Autor -> {nome_autor}\n Editora -> {nome_editora}.\n\n Continue navegando!!\n")
    print('*******************************************\n')
    contador_id += 1
    
#FUNÇÃO PARA CONSULTAR TODOS OS LIVROS
def consultar_todos():
    for livro in livros:
        print(f"ID: {livro['ID']}, Nome do livro: {livro['nome_livro']}, Autor: {livro['nome_autor']}, Editora: {livro['nome_editora']}")

# FUNÇÃO PARA MENU DE CONSULTA DE LIVROS
def consultar_livro():
    print(
        '\n'
        '******************************************\n'
        '--------------Menu Consultar Livro------------\n'
        '\n'
        '1 - Consultar Todos os Livros\n'
        '2 - Consultar Livro por ID\n'
        '3 - Consultar Livro(s) por Autor\n'
        '4 - Retornar\n\n'
        '******************************************\n'
    )
    
    escolha_consulta = input("Por favor digite a opção desejada: ")
    
    if escolha_consulta == '1':
        consultar_todos()
    elif escolha_consulta == '2':
        consultar_por_id()
    elif escolha_consulta == '3':
        consultar_por_autor()
    elif escolha_consulta == '4':
        return
    else:
        print("Opção inválida. Tente novamente.")

# FUNÇÃO PARA CONSULTA DE LIVRO POR ID
def consultar_por_id():
    id_procurado = input("Digite o ID do livro que deseja consultar: ")
    for livro in livros:
        if str(livro['ID']) == id_procurado:
            print(f"ID: {livro['ID']}, Nome do livro: {livro['nome_livro']}, Autor: {livro['nome_autor']}, Editora: {livro['nome_editora']}\n")
            return
    print("Livro não encontrado.")

# FUNÇÃO DE CONSULTA DE LIVRO POR AUTOR
def consultar_por_autor():
    autor_procurado = input("Digite o nome do autor que deseja consultar: ")
    encontrados = False
    for livro in livros:
        if livro['nome_autor'].lower() == autor_procurado.lower():
            print(f"ID: {livro['ID']}, Nome do livro: {livro['nome_livro']}, Autor: {livro['nome_autor']}, Editora: {livro['nome_editora']}")
            encontrados = True
    if not encontrados:
        print("Nenhum livro encontrado para o autor especificado.")

# FUNÇÃO PARA REMOVER LIVRO
def remover_livro():
    id_procurado = input("Digite o ID do livro que deseja remover: ")
    for livro in livros:
        if str(livro['ID']) == id_procurado:
            livros.remove(livro)
            print(f"Livro com ID {id_procurado} removido com sucesso!")
            return
    print("Livro não encontrado.")

# LOOP PRINCIPAL
while True:
    
    if not boas_vindas_exibida:
        print(
            '\n\n\n'
            'Bem Vindo(a) ao Controle de Livros da Jhenyffer Borges\n'
        )
        boas_vindas_exibida = True 

    imprimir_menu()
    
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        cadastrar_livro()
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")