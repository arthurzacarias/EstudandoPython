# Meta = 1000 vendas
# Se valor de vendas >= meta: bonus = 10% valor das vendas, se não bonus = 0

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

if vendas_funcionario1 >= 1000:
    print("O Funcionario 1 ganhou, {} de bonus".format(vendas_funcionario1 * 0.1))
else:
    print("O Funcionario 1 ganhou, {} de bonus".format("0"))
if vendas_funcionario2 >= 1000:
    print("O Funcionario 2 ganhou, {} de bonus".format(vendas_funcionario2 * 0.1))
else:
    print("O Funcionario 2 ganhou, {} de bonus".format("0"))
if vendas_funcionario3 >= 1000:
    print("O Funcionario 3 ganhou, {} de bonus".format(vendas_funcionario3 * 0.1))
else:
    print("O Funcionario 3 ganhou, {} de bonus".format("0"))
