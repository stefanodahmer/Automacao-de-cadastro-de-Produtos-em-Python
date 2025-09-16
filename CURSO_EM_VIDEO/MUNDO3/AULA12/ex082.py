n = int(input("Digite um valor: "))
lista = []
listapares = []
listaimpares = []

lista.append(n)

while True:
	res = str(input("Deseja continuar? [S/N]")).upper().strip()[0]

	while res not in "SN":
		res = str(input("Resposta inválida! Deseja continuar? [S/N]")).upper().strip()[0]

	if res == "N":
		print("TCHAU.")
		break

	lista.append(n)
	n = int(input("Digite um valor: "))
	

for num in lista:
	if num % 2 == 0:
		listapares.append(num)
	else:
		listaimpares.append(num)
		
print("A lista completa é {}".format(lista))
print("A lista de pares é {}".format(listapares))
print("A lista de ímpares é {}".format(listaimpares))


	
	
    