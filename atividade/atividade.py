"""Solução das seis questões da atividade de Algoritmo e Programação."""

from decimal import Decimal
from math import isfinite


def ler_numero(mensagem):
    """Aceita ponto ou vírgula decimal e repete a leitura se houver erro."""
    while True:
        try:
            numero = float(input(mensagem).replace(",", "."))
            if isfinite(numero):
                return numero
        except ValueError:
            pass
        print("Entrada inválida. Digite um número, como 7,5 ou 7.5.")


def reais(valor):
    return f"R$ {valor:.2f}".replace(".", ",")


# Questão 1: coletar e validar as notas com while.
def coletar_notas(qtd_notas):
    notas = []
    contador = 0

    while contador < qtd_notas:
        nota = ler_numero(f"Digite a {contador + 1}ª nota: ")
        if 0 <= nota <= 10:
            notas.append(nota)
            contador += 1
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")

    return notas


# Questão 2: exibir e somar as notas com for.
def calcular_media(lista_notas):
    if not lista_notas:
        raise ValueError("É necessário informar pelo menos uma nota.")

    soma = Decimal("0")
    for nota in lista_notas:
        print(f"Nota: {nota:.2f}")
        soma += Decimal(str(nota))

    media = soma / len(lista_notas)
    return media


# Questão 3: determinar a situação usando if, elif e else.
def determinar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Em Recuperação"
    else:
        return "Reprovado"


# Questão 4: registrar vendas até atingir ou superar a meta.
def registrar_vendas(limite_meta):
    vendas = []
    # Decimal evita erros de soma com centavos, como dez vendas de R$ 0,10.
    total = Decimal("0")
    limite_meta = Decimal(str(limite_meta))

    while total < limite_meta:
        valor = ler_numero("Valor da venda: R$ ")
        if valor > 0:
            vendas.append(valor)
            total += Decimal(str(valor))
            print(f"Acumulado: {reais(total)}")
        else:
            print("Venda inválida! O valor deve ser maior que zero.")

    return vendas


# Questão 5: percorrer as vendas e retornar os resultados em uma tupla.
def analisar_vendas(lista_vendas):
    vendas_altas = 0
    vendas_baixas = 0
    total = Decimal("0")

    for numero, valor in enumerate(lista_vendas, start=1):
        print(f"Operação {numero}: {reais(valor)}")
        total += Decimal(str(valor))
        if valor >= 100:
            vendas_altas += 1
        else:
            vendas_baixas += 1

    ticket_medio = total / len(lista_vendas) if lista_vendas else 0
    print(f"Vendas abaixo de R$ 100,00: {vendas_baixas}")
    return total, ticket_medio, vendas_altas


# Questão 6: classificar o faturamento em relação à meta.
def definir_status_dia(total_faturado, meta_esperada):
    total_faturado = Decimal(str(total_faturado))
    meta_esperada = Decimal(str(meta_esperada))
    if total_faturado >= meta_esperada * Decimal("1.2"):
        return "Superávit Excelente (Bônus para a Equipe)"
    elif total_faturado >= meta_esperada:
        return "Meta Atingida com Sucesso"
    else:
        return "Meta Não Atingida (Abaixo do Esperado)"


def main():
    # Integração das questões 1, 2 e 3.
    print("=== CADASTRO DE NOTAS ===")
    notas = coletar_notas(3)

    print("\n=== BOLETIM ===")
    media = calcular_media(notas)
    situacao = determinar_situacao(media)
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

    # Integração das questões 4, 5 e 6.
    print("\n=== CONTROLE DE VENDAS ===")
    meta = ler_numero("Digite a meta do dia: R$ ")
    while meta <= 0:
        print("A meta deve ser maior que zero.")
        meta = ler_numero("Digite a meta do dia: R$ ")

    vendas = registrar_vendas(meta)

    print("\n=== RELATÓRIO DE VENDAS ===")
    total, ticket_medio, vendas_altas = analisar_vendas(vendas)
    status = definir_status_dia(total, meta)
    print(f"Meta do dia: {reais(meta)}")
    print(f"Total arrecadado: {reais(total)}")
    print(f"Ticket médio: {reais(ticket_medio)}")
    print(f"Vendas a partir de R$ 100,00: {vendas_altas}")
    print(f"Status: {status}")


if __name__ == "__main__":
    main()
