def Fibonacci(n):

	ant = 0
	prox = 1
	aux = 0
	print("Fibonacci: 0")

	while(prox <= n):
		print("Fibonacci: {}".format(prox))
		aux = prox
		prox = prox + ant
		ant = aux
		

n = int(input("Digite um número inteiro positivo: "))
Fibonacci(n)
