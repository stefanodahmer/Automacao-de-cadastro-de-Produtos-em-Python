#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmPercorridos = float(input('Informe a quantidade de km percorridos: '))

diasAlugados = int(input('Informe a quantidade de dias que o carro foi alugado: '))

totaluguel = diasAlugados*60
consumo = kmPercorridos*0.15

valorFinal = totaluguel + consumo

print('Você deve pagar um valor total de {}R$'.format(valorFinal))