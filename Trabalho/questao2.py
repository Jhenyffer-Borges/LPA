pedido = []

# FUNÇÃO PARA IMPRIMIR O MENU
def imprimir_menu():
    print('BEM-VINDO(A) À LOJA DE SORVETES DA JHENYFFER BORGES')
    print("=" * 60)
    print("========================= CARDÁPIO =========================")
    print("=" * 60)
    print("{:<20} {:<30} {:<20}".format("TAMANHO", "CUPUAÇU(CP)", "AÇAÍ(AC)"))
    print("-" * 60)
    print("{:<20} {:<30} {:<20}".format(" P", "R$ 10,00", "R$ 12,00"))
    print("{:<20} {:<30} {:<20}".format(" M", "R$ 15,00", "R$ 17,00"))
    print("{:<20} {:<30} {:<20}".format(" G", "R$ 19,00", "R$ 21,00"))
    print("=" * 60)

# DICIONÁRIO DE VALORES DOS SORVETES
valores = {
    'CP': {'P': 10.00, 'M': 15.00, 'G': 19.00},
    'AC': {'P': 12.00, 'M': 17.00, 'G': 21.00}
}

# FUNÇÃO PARA OBTER O SABOR DESEJADO
def obter_sabor():
    while True:
        opcao = input("Escolha o sabor desejado (CP/ AC): ")
        if opcao in valores:
            return opcao
        else:
            print('Sabor Inválido. Tente novamente.')

# FUNÇÃO PARA OBTER O TAMANHO DESEJADO
def obter_tamanho(opcao):
    while True:
        tamanho = input("Informe o tamanho (P - Pequeno, M - Médio, G - Grande): ")
        if tamanho in valores[opcao]:
            return tamanho
        else:
            print('Tamanho Inválido. Tente novamente.')

# FUNÇÃO PARA CALCULAR O VALOR FINAL DO PEDIDO
def calcular_valor(opcao, tamanho):
    if opcao not in valores or tamanho not in valores[opcao]:
        print('Opção inválida. Por favor, escolha um sabor e tamanho válidos.')
        return None, None, None

    sabor = "Açaí" if opcao == 'AC' else "Cupuaçu"
    valor_base = valores[opcao][tamanho]

    tamanho_descricao = "Pequeno" if tamanho.upper() == 'P' else "Médio" if tamanho.upper() == 'M' else "Grande"

    return sabor, tamanho_descricao, valor_base

# PERGUNTA SE DESEJA MAIS ALGUMA COISA
def obter_adicional():
    while True:
        adicional = input("Deseja adicionar mais alguma coisa?\n 1 - SIM \n 2 - NÃO \n ")
        if adicional == '1':
            return True
        elif adicional == '2':
            return False
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    while True:
        # IMPRIME O MENU
        imprimir_menu()

        # OBTÉM O SABOR ESCOLHIDO
        opcao = obter_sabor()

        # OBTÉM O TAMANHO ESCOLHIDO
        tamanho = obter_tamanho(opcao)

        # CALCULA O VALOR FINAL
        sabor, tamanho_descricao, valor_final = calcular_valor(opcao, tamanho)

        # PERGUNTA SE DESEJA ADICIONAR MAIS ALGO
        adicional = obter_adicional()

        # ARMAZENA AS INFORMAÇÕES DO PEDIDO
        pedido_atual = {
            'Sabor': sabor,
            'Tamanho': tamanho_descricao,
            'Valor': valor_final
        }
        pedido.append(pedido_atual)

        if not adicional:
            break  # Sair do loop se o usuário não quiser mais adicionar itens

    # IMPRIME O RESUMO GERAL DOS PEDIDOS
    print("\nRESUMO GERAL DOS PEDIDOS:")
    print("=" * 30)
    total_valor = 0  
    for idx, pedido_atual in enumerate(pedido, start=1):
        print(f"Pedido {idx}:")
        print("{:<20} {:<30} {:<20}".format("Sabor:", pedido_atual['Sabor'], ""))
        print("{:<20} {:<30} {:<20}".format("Tamanho:", pedido_atual['Tamanho'], ""))
        print("{:<20} {:<30} {:<20}".format("Valor:", "R$ {:.2f}".format(pedido_atual['Valor']), ""))
        print("=" * 30)
        total_valor += pedido_atual['Valor']  

    if len(pedido) > 1:  
        print("\nVALOR TOTAL DOS PEDIDOS: R$ {:.2f}".format(total_valor))