def fatorial(n):
	if(n == 1 or n == 0):
		return 1
	else:
		return n * fatorial(n-1)

v = int(input("Digite um valor para ser calculado o fatorial: "))

print("O fatorial de {} é {}".format(v,fatorial(v)))