numeros = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input("Digite um número entre 0 e 20: "))

if 0 <= n <= 20:
    print(numeros[n-1])
else:
    print("Número inválido! Tente novamente.")