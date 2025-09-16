a = int(input("Digite o valor da primeira reta: "))
b = int(input("Digite o valor da segunda reta: "))
c = int(input("Digite o valor da reta reta: "))

if(a+b > c and a + c > b and b + c > a):
	print("Sim, os valores inseridos podem formar um triangulo!")
	if(a == b == c):
		print("O triângulo é \033[1;32mEQUILÁTERO\033[m!")
	elif(a == b or b == c or a == c):
		print("O triângulo é \033[1;32mISÓSCELES\033[m!")
	elif(a != b and b != c and a != c):
		print("O triângulo é \033[1;32mESCALENO\033[m!")
else:
	print("Os valores inseridos não podem formar um triângulo")