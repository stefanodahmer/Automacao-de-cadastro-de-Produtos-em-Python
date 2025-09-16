import calendar
ano = int(input("Digite um ano: "))

if(calendar.isleap(ano)):
	print("O ano {} é bissexto".format(ano))
else:
	print("O ano {} não é bissexto".format(ano))