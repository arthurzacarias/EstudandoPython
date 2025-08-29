import math

altura = float(input("Altura da parede: "))
largura = float(input("Largura da parede: "))

area = largura * altura
tinta = math.ceil(area/2)

print("Para pintar essa área, seriam necessários: {} litros de tinta".format(tinta))
