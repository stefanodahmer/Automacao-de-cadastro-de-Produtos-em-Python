palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar')

for p in palavras:
	print("Na palavra {} temos as vogais: ".format(p.upper()))
	for letra in p:
		if letra in 'aeiou':
			print(letra, end=' ')
	print('\n')