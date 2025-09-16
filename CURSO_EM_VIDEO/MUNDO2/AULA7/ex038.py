n1 = int(input("Digite o primeiro valor inteiro: "))
n2 = int(input("Digite o segundo valor inteiro: "))

if(n1>n2):
	print("{} é \033[1;32mMAIOR\033[m!".format(n1))
elif(n2>n1):
	print("{} é \033[1;32mMAIOR\033[m!".format(n2))
else:
	print("Os valores são \033[1;31mIGUAIS\033[m!")