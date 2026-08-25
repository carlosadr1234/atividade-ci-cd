# Calculadora em Python com CI/CD

Este projeto consiste em uma calculadora desenvolvida em Python, com operações matemáticas básicas e avançadas. O projeto utiliza testes automatizados e GitHub Actions para demonstrar conceitos de Integração Contínua e Entrega Contínua.

## Funcionalidades

A calculadora possui operações como:

- Soma
- Subtração
- Multiplicação
- Divisão
- Potência
- Raiz quadrada
- Porcentagem
- Fatorial
- Logaritmo
- Seno
- Cosseno
- Tangente
- Média

## Testes automatizados

O arquivo `test_calculadora.py` contém testes automatizados para verificar o funcionamento das operações da calculadora.

Os testes também verificam situações de erro, como divisão por zero e operações matemáticas inválidas.

## Pipeline CI/CD

### 1. O que representa a etapa de CI neste projeto?

A etapa de Continuous Integration (CI) executa automaticamente os testes do projeto sempre que uma alteração é enviada ao repositório.

### 2. O que impede a execução do Continuous Delivery quando existe um defeito?

O Continuous Delivery depende do sucesso da etapa de CI. Quando algum teste falha, o CI apresenta falha e o Delivery não é executado.

### 3. Qual seria a próxima etapa necessária para transformar este pipeline em Continuous Deployment?

Seria necessário adicionar uma etapa de implantação automática, que enviaria a aplicação para um ambiente de produção depois que os testes fossem aprovados.

## Tecnologias utilizadas

- Python
- Pytest
- GitHub
- GitHub Actions
- Continuous Integration
- Continuous Delivery
