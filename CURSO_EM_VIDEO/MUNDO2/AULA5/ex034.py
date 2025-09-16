salario = float(input("Digite seu salario: "))
salariof = 0

if(salario>1250):
	salariof = salario*1.10
else:
	salariof = salario*1.15

print("O salário final é de {:.2f}R$".format(salariof))

	