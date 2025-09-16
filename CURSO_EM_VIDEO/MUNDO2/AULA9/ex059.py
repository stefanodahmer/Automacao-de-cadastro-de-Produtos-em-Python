n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
res = 0

opcao=0 


while(opcao != 5):
	opcao=int(input("Informe a operação desejada:\n[1] -> Somar\n[2] -> Multiplicar\n[3] -> Maior\n[4] -> Novos números\n[5] -> Sair\n"))
	
	if(opcao==1):
		res = n1+n2
		print("A soma entre {} e {} é {}\n".format(n1,n2,res))
	elif(opcao==2):
		res = n1*n2
		print("A multiplicação entre {} e {} é {}\n".format(n1,n2,res))
	elif(opcao==3):
		print("O maior número entre os dois é {}\n".format(max(n1,n2)))
	elif(opcao==4):
		n1 = int(input("Digite o primeiro número: "))
		n2 = int(input("Digite o segundo número: "))
	elif(opcao==5):
		print("Finalizando...")
	else:
		print("Digite uma opção válida")
		
		
	