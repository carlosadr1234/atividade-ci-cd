import pytest

from calculadora import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    potencia,
    raiz_quadrada,
    porcentagem,
    fatorial,
    logaritmo,
    seno,
    cosseno,
    tangente,
    media,
    calculo_expressao,
)


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(10, 4) == 6


def test_multiplicar():
    assert multiplicar(5, 4) == 20


def test_dividir():
    assert dividir(10, 2) == 5


def test_divisao_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_potencia():
    assert potencia(2, 3) == 8


def test_raiz_quadrada():
    assert raiz_quadrada(144) == 12


def test_raiz_quadrada_negativa():
    with pytest.raises(ValueError):
        raiz_quadrada(-1)


def test_porcentagem():
    assert porcentagem(200, 15) == 30


def test_fatorial():
    assert fatorial(5.0) == 120


def test_fatorial_invalido():
    with pytest.raises(ValueError):
        fatorial(-5.0)


def test_logaritmo():
    assert logaritmo(100) == 2


def test_seno():
    assert seno(30) == pytest.approx(0.5)


def test_cosseno():
    assert cosseno(60) == pytest.approx(0.5)


def test_tangente():
    assert tangente(45) == pytest.approx(1.0)


def test_media():
    assert media([10, 20, 30]) == 20


def test_media_vazia():
    with pytest.raises(ValueError):
        media([])


def test_calculo_expressao():
    assert calculo_expressao(10, "+", 5) == 15
    assert calculo_expressao(10, "-", 5) == 5
    assert calculo_expressao(10, "*", 5) == 50
    assert calculo_expressao(10, "/", 5) == 2


def test_operador_invalido():
    with pytest.raises(ValueError):
        calculo_expressao(10, "%", 5) if n < 0 or not n.is_integer():
        raise ValueError("O fatorial deve ser de um número inteiro não negativo.")
    return math.factorial(int(n))


def logaritmo(a, base=10):
    if a <= 0:
        raise ValueError("O número deve ser maior que zero.")
    if base <= 0 or base == 1:
        raise ValueError("A base deve ser positiva e diferente de 1.")
    return math.log(a, base)


def seno(graus):
    return math.sin(math.radians(graus))


def cosseno(graus):
    return math.cos(math.radians(graus))


def tangente(graus):
    return math.tan(math.radians(graus))


def media(valores):
    if not valores:
        raise ValueError("A lista de valores não pode estar vazia.")
    return sum(valores) / len(valores)


def calculo_expressao(a, operador, b):
    operacoes = {
        "+": somar,
        "-": subtrair,
        "*": multiplicar,
        "/": dividir,
        "^": potencia
    }

    if operador not in operacoes:
        raise ValueError("Operador inválido.")

    return operacoes[operador](a, b)
