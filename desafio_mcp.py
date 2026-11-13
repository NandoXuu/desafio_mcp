from datetime import datetime


def calcular_vendas(vendas):
    total = 0
    quantidade = 0

    for venda in vendas:
        total += venda
        quantidade += 1

    media_venda = total / quantidade if quantidade > 0 else 0

    return {
        "total": total,
        "quantidade": quantidade,
        "media": media_venda
    }


def gerar_relatorio(vendas):
    resultado = calcular_vendas(vendas)

    print("\n========== RELATÓRIO DE VENDAS ==========")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Quantidade de vendas: {resultado['quantidade']}")
    print(f"Faturamento total: R$ {resultado['total']:.2f}")
    print(f"Média por venda: R$ {resultado['media']:.2f}")
    print("=========================================\n")


def main():
    vendas = [
        150.50,
        89.90,
        230.00,
        45.75,
        310.20,
        120.00
    ]

    gerar_relatorio(vendas)


if __name__ == "__main__":
    main()
