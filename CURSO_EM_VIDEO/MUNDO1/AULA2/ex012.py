altura = float(input("Insira a altura da parede: "))
largura = float(input("Insira  largura da parede: "))

area = altura*largura
qntTinta = area/2

print("Você precisará de {:.1f}L de tinta".format(qntTinta))