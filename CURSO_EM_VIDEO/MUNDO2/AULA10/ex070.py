nome = ''
valor = 0
total = 0
nomemaisbarato = ''
valormaisbarato = 0
acimademil = 0
res = ''
continua = True

print("===============================================")
print("                LOJA SUPER BARATÃO              ")
print("===============================================")

while continua:
	nome = str(input("Digite o nome do produto: "))
	valor = float(input("Digite o valor do produto: "))

	while valor < 0:
		print("Valor inválido. Tente novamente")
		valor = float(input("Digite o valor do produto: "))
		

	total = total + valor

	if valor >= 1000:
		acimademil = acimademil + 1

	if valormaisbarato == 0 or valor < valormaisbarato:
		nomemaisbarato = nome
		valormaisbarato = valor

	res = str(input("Deseja continuar? Sim ou Não [S/N]")).upper().strip()[0]   
	while res not in 'SN':
		res = str(input("Deseja continuar? Sim ou Não [S/N]")).upper().strip()[0]

	if(res != 'S'):
		continua = False
		break

print("Total de gastos: {}\nProdutos mais de R$1000.00: {}\nNome do produto mais barato: {}".format(total, acimademil, nomemaisbarato))



	
	
	