import random

numero = random.randint(0,5)

chute = int(input("Digite seu chute: "))

if(chute == numero):
    print("Você acertou! O número era {}".format(chute))
else:
    print("Você errou! O número era {}".format(numero))