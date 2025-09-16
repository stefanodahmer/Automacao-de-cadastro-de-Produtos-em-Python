a_zero = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))

for i in range(0,10):
	print("a{} = {}".format(i,a_zero + r*i))

print("FIM")
	