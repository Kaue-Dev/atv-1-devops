import pytest

from calculadora import calcular_total


def test_total_sem_desconto():
    itens = [(10.0, 2), (5.0, 1)]

    assert calcular_total(itens) == 25.0


def test_total_com_dez_por_cento_de_desconto():
    itens = [(100.0, 2), (50.0, 1)]

    assert calcular_total(itens, desconto_percentual=10) == 225.0


def test_total_com_cupom_devops10_adiciona_dez_por_cento():
    itens = [(100.0, 1)]

    assert calcular_total(itens, desconto_percentual=10, cupom_desconto="DEVOPS10") == 80.0


def test_total_com_cupom_devops10_minusculo():
    itens = [(100.0, 1)]

    assert calcular_total(itens, cupom_desconto="devops10") == 90.0


def test_total_com_cupom_invalido():
    itens = [(100.0, 1)]

    assert calcular_total(itens, cupom_desconto="DEVOPS") == 100.0


def test_cupom_freteexpress_zera_frete_quando_total_com_desconto_excede_cinquenta():
    itens = [(100.0, 1)]

    assert calcular_total(
        itens,
        desconto_percentual=10,
        cupom_desconto="FRETEEXPRESS",
        frete_express=15,
    ) == 90.0


def test_cupom_freteexpress_nao_zera_frete_quando_total_com_desconto_igual_cinquenta():
    itens = [(50.0, 1)]

    assert calcular_total(
        itens,
        cupom_desconto="FRETEEXPRESS",
        frete_express=15,
    ) == 65.0


def test_cupom_freteexpress_nao_zera_frete_quando_total_com_desconto_menor_que_cinquenta():
    itens = [(40.0, 1)]

    assert calcular_total(
        itens,
        cupom_desconto="FRETEEXPRESS",
        frete_express=15,
    ) == 55.0


def test_cupom_freteexpress_nao_altera_desconto_percentual():
    itens = [(100.0, 1)]

    assert calcular_total(
        itens,
        cupom_desconto="FRETEEXPRESS",
    ) == 100.0


def test_desconto_invalido():
    with pytest.raises(ValueError):
        calcular_total([(100.0, 1)], desconto_percentual=110)
