# Input produto, categoria e quantidade
# Quantidade mínima para as categorias:
# alimentos -> minimo 50
# bebidas -> mínimo 75
# limpeza -> mínimo 30

produto = input("Digite o nome do produto: ")
categoria = input("Digite a categoria do produto (alimentos, bebidas ou limpeza): ").lower()
quantidade = input("Digite a quantidade do produto: ")

if produto and categoria and quantidade:
    quantidade = int(quantidade)
    if categoria == "alimentos" and quantidade < 50:
        print("Solicitar mais unidades de {}".format(produto))
    elif categoria == "bebidas" and quantidade < 75:
        print("Solicitar mais unidades de {}".format(produto))
    elif categoria == "limpeza" and quantidade < 30:
        print("Solicitar mais unidades de {}".format(produto))
else:
    print("Preencha corretamente todos os campos!")