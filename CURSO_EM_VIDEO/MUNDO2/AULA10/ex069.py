continua = True
op = ''
maiores = 0
homens = 0
velhas = 0

while continua:
	idade = int(input("Digite a idade da pessoa: "))
	sexo = str(input("Digite o sexo [M/F]: ")).upper().strip()[0]

	while sexo not in 'MF':
		sexo = str(input("Digite o sexo [M/F]: ")).upper().strip()[0]

	
	if(idade >= 18):
		maiores = maiores + 1
	
	if(sexo == 'M'):
		homens = homens + 1

	if(sexo == 'F' and idade >= 40):
		velhas = velhas + 1

	
	op = str(input("Continuar? Sim ou Não [S/N]: ")).upper().strip()[0]
	
	if(op == 'N'):
		continua = False
		break
	
	
print("Total de pessoas com mais de 18 anos: {}".format(maiores))
print("Total de homens cadastrados: {}".format(homens))
print("Total de mulheres com mais de 40 anos: {}".format(velhas))