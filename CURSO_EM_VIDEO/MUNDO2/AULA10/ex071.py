valor = 0
resto = 0
notascinquenta = 0
notasvinte = 0
notasdez = 0
notasum = 0

print("Banco CEV")

valor = int(input("Qual valor você quer sacar? R$"))
aux = valor

while aux != 0:

	if aux >= 50:
		aux = aux - 50
		notascinquenta = notascinquenta + 1
	
	elif aux >= 20:
		aux = aux - 20
		notasvinte = notasvinte + 1

	elif aux >= 10:
		aux = aux - 10
		notasdez = notasdez + 1

	elif aux >= 1:
		aux = aux - 1
		notasum = notasum + 1
		
print("Total de {} cédulas de R$50".format(notascinquenta))
print("Total de {} cédulas de R$20".format(notasvinte))
print("Total de {} cédulas de R$10".format(notasdez))
print("Total de {} cédulas de R$1".format(notasum))
print("Volte sempre ao Banco CEV! Tenha um bom dia!")

	
	
	

	
		
		
		

	

    
   