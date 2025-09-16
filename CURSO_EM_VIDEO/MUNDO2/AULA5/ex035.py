a = int(input("Digite o valor da primeira reta: "))
b = int(input("Digite o valor da segunda reta: "))
c = int(input("Digite o valor da reta reta: "))

if(a+b > c and a + c > b and b + c > a):
	print("Sim, os valores inseridos podem formar um triangulo!")
else:
	print("Os valores inseridos não podem formar um triângulo")