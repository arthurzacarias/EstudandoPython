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