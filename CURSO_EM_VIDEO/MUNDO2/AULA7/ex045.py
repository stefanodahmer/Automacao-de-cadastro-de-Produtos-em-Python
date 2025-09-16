import random

# crie um programa que faça o computador ogar okenpo contra você
# pedra, papel, tesoura

itens = ("Pedra", "Papel", "Tesoura")
computador = random.randint(0, 2)

escolha = int(input("Escolha entre \n[0] Pedra\n[1] Papel\n[2] Tesoura\n"))

print("O computador escolheu: {}".format(itens[computador]))

if(0 <= escolha < 3 ):
    if(escolha == computador):
            print("EMPATE")

    elif(escolha == 0 and computador == 2):
            print("Você venceu")

    elif(escolha == 1 and computador == 0):
            print("Você venceu")

    elif(escolha == 2 and computador == 1):
            print("Você venceu")

    else:
            print("Você perdeu")

else:
    print("Digite uma opçao válida ANIMAL")


