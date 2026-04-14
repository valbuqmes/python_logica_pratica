#Uma loja registrou suas vendas em uma lista de dicionários. Cada venda contém:
#nome do produto, quantidade vendida e preço unitário.
#• Percorra todas as vendas e calcule o valor total de cada venda (quantidade × preço).
#• Exiba apenas as vendas com valor maior que R$ 50,00.
#• Calcule e exiba o faturamento total da loja.
#• Identifique e exiba qual produto mais faturou.

vendas = [
    {"produto": "Notebook", "quantidade": 2, "preco": 3500.00},
    {"produto": "Mouse", "quantidade": 5, "preco": 50.00},
    {"produto": "Teclado", "quantidade": 3, "preco": 120.00},
    {"produto": "Monitor", "quantidade": 1, "preco": 900.00}
]
valor_vendas = 0
faturamento = 0
for i in vendas:
    valor_vendas = i['quantidade'] * i['preco']
    faturamento = faturamento + valor_vendas
    if valor_vendas > 50:
        print(valor_vendas)

print(f"Faturamento total: {faturamento}")