# juntar listas

produtos = ["apple tv", "mac", "iphone X", "iphone 17", "ipods"]
novos_produtos = ["iphone 12", "iglasses"]

todos_produtos = produtos + novos_produtos
print(todos_produtos)

# organizando os itens da lista
produtos.sort(reverse=True)
print(produtos)

# printar com enter
print("\n".join(todos_produtos))

# listas de listas
vendedores = ["João", "Maria", "Pedro"]
produtos = ["iPhone", "iPad"]
vendas = [
    [1500, 2000],  # Vendas de João
    [3000, 2500],  # Vendas de Maria
    [4000, 3500]   # Vendas de Pedro
]

vendas_joao_iphone = vendas[0][0]