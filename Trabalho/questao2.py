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

if __name__ == "__main__":
    # IMPRIME O MENU
    imprimir_menu()

    # OBTÉM O SABOR ESCOLHIDO
    opcao = obter_sabor()

    # OBTÉM O TAMANHO ESCOLHIDO
    tamanho = obter_tamanho(opcao)

    # CALCULA O VALOR FINAL
    sabor, tamanho_descricao, valor_final = calcular_valor(opcao, tamanho)

    # IMPRIME O RESUMO DO PEDIDO
    if sabor is not None and tamanho_descricao is not None and valor_final is not None:
        print("\nRESUMO DO PEDIDO:")
        print("=" * 30)
        print("{:<20} {:<30} {:<20}".format("Sabor:", sabor, ""))
        print("{:<20} {:<30} {:<20}".format("Tamanho:", tamanho_descricao, ""))
        print("{:<20} {:<30} {:<20}".format("Valor:", "R$ {:.2f}".format(valor_final), ""))
        print("=" * 30)
    else:
        print("Opção inválida. Por favor, escolha um sabor e tamanho válidos.")
