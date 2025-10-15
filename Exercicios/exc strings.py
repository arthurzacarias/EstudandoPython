#1 CPF
cpf = input("Digite o seu CPF (apenas números)")

if len(cpf) == 11 and cpf.isnumeric:
    print(cpf)
else:
    print("O CPF deve conter 11 digitos e apenas números")

