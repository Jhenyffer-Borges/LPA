# FUNÇÃO PARA IMPRIMIR AS BOAS-VINDAS
def imprimir_boas_vindas():
    print("Bem-vindo(a) ao aplicativo de vendas da Jhenyffer Borges!")

# FUNÇÃO PARA OBTER O VALOR UNITÁRIO DO PRODUTO
def obter_valor_unitario():
    return float(input("Digite o valor unitário do produto: "))

# FUNÇÃO PARA OBTER A QUANTIDADE DO PRODUTO
def obter_quantidade():
    return int(input("Digite a quantidade do produto: "))

# FUNÇÃO PARA CALCULAR O VALOR TOTAL SEM DESCONTO
def calcular_valor_total_sem_desconto(valor_unitario, quantidade):
    return valor_unitario * quantidade

# FUNÇÃO PARA APLICAR DESCONTOS COM BASE NO VALOR TOTAL SEM DESCONTO
def aplicar_desconto(valor_total_sem_desconto):
    if valor_total_sem_desconto < 1000:
        return 0
    elif valor_total_sem_desconto < 3000:
        return 3
    elif valor_total_sem_desconto < 5000:
        return 5
    else:
        return 8

# FUNÇÃO PARA CALCULAR O VALOR TOTAL COM DESCONTO
def calcular_valor_total_com_desconto(valor_total_sem_desconto, desconto_percentual):
    desconto_decimal = desconto_percentual / 100
    return valor_total_sem_desconto * (1 - desconto_decimal)

# FUNÇÃO PARA IMPRIMIR O RESUMO DA COMPRA
def imprimir_resumo_compra(valor_total_sem_desconto, desconto_percentual, valor_total_com_desconto):
    print("Resumo da compra:")
    print(f"Valor total sem desconto: R${valor_total_sem_desconto}")
    print(f"Desconto aplicado: {desconto_percentual}%")
    print(f"Valor total com desconto: R${valor_total_com_desconto}")

    if valor_total_sem_desconto > 1000 and desconto_percentual > 0:
        print("Parabéns! Você recebeu um desconto especial na sua compra.")

if __name__ == "__main__":
    # CHAMA A FUNÇÃO DE BOAS-VINDAS
    imprimir_boas_vindas()

    # CHAMA AS FUNÇÕES PARA OBTER VALOR UNITÁRIO E QUANTIDADE
    valor_unitario = obter_valor_unitario()
    quantidade = obter_quantidade()

    # CALCULA O VALOR TOTAL SEM DESCONTO
    valor_total_sem_desconto = calcular_valor_total_sem_desconto(valor_unitario, quantidade)

    # APLICA O DESCONTO
    desconto_percentual = aplicar_desconto(valor_total_sem_desconto)

    # CALCULA O VALOR TOTAL COM DESCONTO
    valor_total_com_desconto = calcular_valor_total_com_desconto(valor_total_sem_desconto, desconto_percentual)

    # IMPRIME O RESUMO DA COMPRA
    imprimir_resumo_compra(valor_total_sem_desconto, desconto_percentual, valor_total_com_desconto)
