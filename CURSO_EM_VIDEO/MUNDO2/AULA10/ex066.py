import random
jogador = 0
computador = 0
perdeu = False
op = ''

while not perdeu:
	jogador = int(input("Digite um valor: "))
	computador = random.randint(0,5)
	soma = jogador + computador
	op = str(input("Par ou Ímpar? [P/I]: ")).upper().strip()[0]

	if(op == "P" and soma % 2 == 0):
		print("Você jogou {} e o computador {}. Total de {} DEU PAR".format(jogador,computador,soma))
		print("Você VENCEU!")
		print("Vamos jogar novamente...")

	elif(op == "I" and soma % 2 == 1):
		print("Você jogou {} e o computador {}. Total de {} DEU ÍMPAR".format(jogador,computador,soma))
		print("Você VENCEU!")
		print("Vamos jogar novamente...")

	elif(op == "I" and soma % 2 == 0):
		print("Você jogou {} e o computador {}. Total de {} DEU PAR".format(jogador,computador,soma))
		print("Você PERDEU!")
		break

	elif(op == "P" and soma % 2 == 1):
		print("Você jogou {} e o computador {}. Total de {} DEU ÍMPAR".format(jogador,computador,soma))
		print("Você PERDEU!")
		break
	else:
		print("Sla qq deu. Parei")
		break
