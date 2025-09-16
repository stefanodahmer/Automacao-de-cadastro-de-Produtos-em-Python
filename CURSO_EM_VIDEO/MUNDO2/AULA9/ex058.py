import random

numero = random.randint(0,5)
tentativas = 0
chute = int(input("Digite seu chute: "))

while(chute != numero):
    chute = int(input("Digite seu chute: "))
    tentativas = tentativas + 1

print("Você acertou, o número era {}. Você tentou {} vezes.".format(chute, tentativas))

