import math


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def potencia(a, b):
    return a ** b


def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Não existe raiz quadrada real de número negativo.")
    return math.sqrt(a)


def porcentagem(valor, percentual):
    return valor * percentual / 100


def fatorial(n):
    if n < 0 or not n.is_integer():
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
