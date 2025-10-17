
"""
# Exercícios

## 1. Faturamento do Melhor e do Pior Mês do Ano

Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?
"""

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

# gera uma lista com todas as vendas do ano
vendas_ano = vendas_1sem + vendas_2sem

# encontra o mes com maior valor de vendas
valor_maiormes = max(vendas_ano)
# encontra o indice do mes com maior valor de vendas
i = vendas_ano.index(valor_maiormes)
melhor_mes = meses[i]
print(f'O melhor mês do ano foi {melhor_mes} com {valor_maiormes} vendas')

# encontra o mes com menor valor de vendas
valor_menormes = min(vendas_ano)
# encontra o indice do mes com menor valor de vendas
j = vendas_ano.index(valor_menormes)
pior_mes = meses[j]
print(f'O pior mês do ano foi {pior_mes} com {valor_menormes} vendas')

"""## 2. Continuação

Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista
"""
sum_vendas = sum(vendas_ano)
percentual_melhor = (valor_maiormes / sum_vendas) * 100
print(f'O faturamento total do ano foi de {sum_vendas} e o melhor mês representou {percentual_melhor:.2f}% do faturamento total.')


"""## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

Dica: o método remove retira um item da lista.
"""
vendas_ano_organizada = sorted(vendas_ano, reverse=True)

top3 = [vendas_ano_organizada[0], vendas_ano_organizada[1], vendas_ano_organizada[2]]
print(top3)