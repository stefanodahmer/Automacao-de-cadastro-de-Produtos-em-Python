n = 0
lista = []
n = int(input("Digite um valor: "))
lista.append(n)
res = ' '

while True:
	res = str(input("Deseja continuar? [S/N]")).upper().strip()[0] 
	if res != "S":
		break

	n = int(input("Digite um valor: "))
	if n in lista:
		print("A lista já contém esse valor. Ele não foi adicionado!")
	else:
		lista.append(n)

lista.sort()
print("Você digitou os valores {}".format(lista))
		

	
	