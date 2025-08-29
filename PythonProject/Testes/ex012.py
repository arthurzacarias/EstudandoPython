import math

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos KM rodados? "))

kilometros = math.ceil(km)

custoDias = dias * 60
custoKm = kilometros * 0.15

print("O total a pagar é: R$: {:.2f}".format(custoDias + custoKm))