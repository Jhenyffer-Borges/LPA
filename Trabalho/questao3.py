#CRIANDO O MENU
def imprimir_menu():
    print(
        'Bem Vindo(a) a Loja de Informática da Jhenyffer Borges\n'
        '\n'
        '---Serviços---\n'
        '\n'
        'DIG - Digitalização\n'
        'ICO - Impressão Colorida\n'
        'IPB - Impressão Preto e Branco\n'
        'FOT - Fotocópia\n'
    )

imprimir_menu()

# CRIANDO DICIONÁRIO PARA VALORES DE SERVIÇOS
valores = {
    'DIG': 1.10,
    'ICO': 1.00,
    'IPB': 0.40,
    'FOT': 0.20
}

# INPUT DE SELEÇÃO DE SERVIÇO DESEJADO
def obter_servico():
    while True:
        opcao = input("Escolha o serviço desejado (DIG/ICO/IPB/FOT): ").upper()
        if opcao in valores:
            return opcao
        else:
            print('Serviço inválido. Entre com o tipo de serviço desejado novamente.')

# INPUT PARA O CLIENTE ESCOLHER O NUMERO DE PAGINAS
servico_escolhido = obter_servico()

def obter_quantidade():
    while True:
        quantidade = int(input("Digite o numero de paginas): "))
        if quantidade < 10:
            return quantidade, 0  # Sem desconto
        elif 10 <= quantidade < 100:
            return int(quantidade * 0.9), 10  # Desconto de 10%
        elif 100 <= quantidade < 1000:
            return int(quantidade * 0.85), 15  # Desconto de 15%
        elif 1000 <= quantidade < 10000:
            return int(quantidade * 0.8), 20  # Desconto de 20%
        else:
            print('Não aceitamos pedidos com mais de 10000 páginas. Por favor, escolha um número menor de páginas.')


quantidade, desconto = obter_quantidade()

#INPUT PARA ESCOLHER SE DESEJA SERVIÇO ADICIONAL

def obter_adicional():
    while True:
        adicional = input("Deseja adicionar mais algum serviço?\n 1 - Encadernação simples - R$ 10.00 \n 2 - Encadernação Capa Dura - R$ 25.00 \n 0 - Não desejo mais nada: ")
        if adicional in ['1', '2', '0']:
            return adicional
        else:
            print('Valor inválido. Tente novamente.')

adicional = obter_adicional()

# CRIANDO DICIONÁRIO PARA VALORES DE SERVIÇOS ADICIONAIS
valores_adicionais = {
    '1': 10.00,
    '2': 25.00,
    '0': 0.00
}

# CALCULANDO VALOR TOTAL
valor_original = valores[servico_escolhido] * quantidade + valores_adicionais[adicional]
valor_final = valor_original - (valor_original * desconto / 100)

# IMPRIME ESCOLHAS DO CLIENTE
print(f"Você escolheu o serviço: {servico_escolhido} com o valor original de R${valor_original:.2f} para {quantidade} páginas.")
print(f"Desconto aplicado: {desconto}%")
print(f"Serviço adicional escolhido: {adicional} - Valor: R${valores_adicionais[adicional]:.2f}")
print(f"Valor final com desconto: R${valor_final:.2f}")
