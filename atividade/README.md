# Atividade de Algoritmo e Programação — 28/10/2026

O arquivo [`atividade.py`](atividade.py) resolve as seis questões do PDF. Ele é um programa Python de terminal: você digita os dados e vê os resultados em texto.

## Como executar

1. Instale o Python 3, caso ainda não tenha.
2. Salve o arquivo `atividade.py` em uma pasta.
3. Abra o terminal nessa pasta.
4. Execute `python atividade.py`. Dependendo da instalação, o comando pode ser `python3 atividade.py` ou, no Windows, `py atividade.py`.
5. Digite uma informação por vez e pressione Enter. Pode usar vírgula ou ponto nos números decimais, por exemplo, `7,5` ou `7.5`. Ao informar dinheiro, digite somente o número, sem `R$` nem separador de milhar.

O programa usa somente a biblioteca padrão do Python. Não é necessário instalar pacotes.

## O que acontece ao executar

Primeiro, o programa solicita três notas válidas e imprime o boletim. Depois, solicita uma meta de vendas positiva e registra as vendas até atingir ou ultrapassar essa meta. Ao final, imprime o relatório comercial.

## Como construir e entender o programa

### 1. Coletar as notas: `coletar_notas(qtd_notas)`

Criamos uma lista vazia com `notas = []` e um contador que começa em zero. O `while contador < qtd_notas` repete o cadastro até completar a quantidade pedida.

O teste `0 <= nota <= 10` aceita inclusive 0 e 10. Quando a nota é válida, `notas.append(nota)` a coloca na lista e `contador += 1` avança o cadastro. Se for inválida, mostramos o erro sem aumentar o contador. Por isso, a mesma nota é solicitada novamente.

O `return notas` entrega a lista para a próxima etapa.

### 2. Calcular a média: `calcular_media(lista_notas)`

A variável `soma` começa em zero. O `for nota in lista_notas` visita cada nota, mostra seu valor e o acrescenta à soma com `soma += Decimal(str(nota))`. Essa conversão mantém a precisão decimal durante o cálculo.

Depois, calculamos `soma / len(lista_notas)`. O `len` informa quantas notas existem. Por exemplo, para 8, 6 e 7, a média é `(8 + 6 + 7) / 3 = 7`.

A verificação inicial impede uma divisão por zero se alguém chamar essa função com uma lista vazia.

### 3. Determinar a situação: `determinar_situacao(media)`

As condições são avaliadas em ordem:

- Média maior ou igual a 7: `Aprovado`.
- Caso contrário, média maior ou igual a 5: `Em Recuperação`.
- Nos demais casos: `Reprovado`.

Quando o Python chega ao `elif`, a condição anterior já falhou. Portanto, essa segunda faixa corresponde a `5 <= media < 7`.

O PDF escreve a faixa de recuperação até 6,9. Usamos "menor que 7" para também cobrir médias como 6,95. A classificação usa a média calculada; `:.2f` apenas mostra duas casas decimais na tela.

### 4. Registrar as vendas: `registrar_vendas(limite_meta)`

Criamos uma lista de vendas e um total inicialmente igual a zero. O `while total < limite_meta` mantém o cadastro enquanto falta dinheiro para atingir a meta.

Cada valor positivo é adicionado à lista e ao total. Valores iguais ou menores que zero exibem um aviso e não alteram os dados.

Exemplo: com meta de 300 e vendas de 50, 100 e 150, o total chega a 300 e o laço termina. A lista retornada é `[50.0, 100.0, 150.0]`.

### 5. Analisar as vendas: `analisar_vendas(lista_vendas)`

Inicializamos `vendas_altas`, `vendas_baixas` e `total` em zero. O `for` percorre a lista. `enumerate(lista_vendas, start=1)` fornece o número da operação, começando em 1, junto com o valor vendido.

Uma venda de exatamente R$ 100,00 já conta como alta. Abaixo disso, conta como baixa. O ticket médio é o total dividido pela quantidade de vendas.

A função retorna três resultados em uma tupla:

```python
return total, ticket_medio, vendas_altas
```

O programa principal recebe esses resultados em três variáveis:

```python
total, ticket_medio, vendas_altas = analisar_vendas(vendas)
```

A quantidade de vendas baixas também é exibida. Para uma lista vazia, o ticket médio fica em zero, evitando divisão por zero.

### 6. Classificar o dia: `definir_status_dia(total_faturado, meta_esperada)`

Multiplicar a meta por `Decimal("1.2")` calcula 120% dela, isto é, a meta mais 20%.

- Faturamento a partir de 120% da meta: `Superávit Excelente (Bônus para a Equipe)`.
- Faturamento a partir da meta e abaixo de 120%: `Meta Atingida com Sucesso`.
- Faturamento abaixo da meta: `Meta Não Atingida (Abaixo do Esperado)`.

Por exemplo, se a meta é R$ 300,00, o bônus começa em R$ 360,00. O intervalo intermediário também inclui 119,5% da meta, evitando a lacuna entre os 119% e 120% citados no PDF.

Como o registro de vendas só termina quando a meta é alcançada, a mensagem "Meta Não Atingida" pode ser observada chamando essa função diretamente com um total menor que a meta.

### Funções auxiliares e execução principal

`ler_numero(mensagem)` centraliza a leitura pelo teclado. `input` recebe texto; `replace` troca vírgula por ponto; `float` converte o texto em número. O `try/except` trata entradas como `abc`, e `isfinite` rejeita valores especiais como infinito. Uma entrada inválida é solicitada novamente.

`reais(valor)` formata um valor com duas casas decimais e vírgula: por exemplo, `100.5` aparece como `R$ 100,50`.

Nos cálculos de dinheiro e da média das notas, usamos `Decimal`, da biblioteca padrão. Ele permite somar valores decimais sem os pequenos erros de representação de `float`: por exemplo, dez vendas de R$ 0,10 atingem exatamente R$ 1,00, e as notas 6,6, 9,7 e 4,7 produzem média 7. `Decimal(str(valor))` transforma o número em sua representação decimal. A leitura pelo teclado continua usando `float`.

`main()` conecta as seis questões, passando o resultado de uma função como argumento para a próxima. A meta é digitada pelo usuário porque o enunciado não fixa um valor.

O trecho final executa `main()` quando o arquivo é iniciado diretamente:

```python
if __name__ == "__main__":
    main()
```

## Exemplo de uso

Informe as notas `8`, `6` e `7`. Depois, informe a meta `300` e as vendas `50`, `100` e `150`.

Resultados esperados:

```text
Média: 7.00
Situação: Aprovado
...
Vendas abaixo de R$ 100,00: 1
Meta do dia: R$ 300,00
Total arrecadado: R$ 300,00
Ticket médio: R$ 100,00
Vendas a partir de R$ 100,00: 2
Status: Meta Atingida com Sucesso
```

Para conferir a validação, tente uma nota `11` ou `-1`, uma venda `0` ou `-5`, ou um texto como `abc`. O programa deve explicar o erro e pedir uma nova entrada.
