n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))



if(n1 <= n2 and n1 < n3):
	print("O menor número é {} e o maior é {}".format(n1, max(n2, n3)))
elif(n2 <= n1 and n2 < n3):
	print("O menor número é {} e o maior é {}".format(n2, max(n1, n3)))
else: 
	print("O menor número é {} e o maior é {}".format(n3, max(n1, n2)))