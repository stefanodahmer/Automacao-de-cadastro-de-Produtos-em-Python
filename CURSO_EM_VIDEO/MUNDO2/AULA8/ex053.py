frase = str(input("Digite uma frase: ")).strip().upper()
frase_original = frase
frase = frase.replace(" ", "")
aux = 0
bool_aux = True

for i in range(len(frase) - 1, 0, -1):

	if(frase[i] == frase[aux]):
		aux+=1
		continue
	else:	
		bool_aux = False
		break

if(bool_aux):
	print("A frase {} é palíndromo".format(frase_original))
else:
	print("Não é palíndromo")

		
		
		
		

	
