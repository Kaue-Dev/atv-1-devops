def calcular_total(itens, desconto_percentual=0, cupom_desconto=None):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)
    """
    if cupom_desconto and cupom_desconto.lower() == "devops10":
        desconto_percentual += 10

    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    valor_do_desconto = subtotal * desconto_percentual / 100
    total = subtotal - valor_do_desconto

    return round(total, 2)
