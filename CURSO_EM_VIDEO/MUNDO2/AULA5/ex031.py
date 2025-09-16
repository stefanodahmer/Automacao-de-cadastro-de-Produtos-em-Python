dist = float(input("Digite a distância total da viagem: "))
valor = 0

if(dist>200):
	valor = dist*0.45
else:
	valor = dist*0.50

print("O valor cobrado é de R$ {:.2f}".format(valor))