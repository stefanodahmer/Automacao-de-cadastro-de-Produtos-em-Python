maior = 0
menor = 0

for i in range(1,6):
    peso = float(input("Digite o peso: "))
    if(peso > maior):
        maior = peso
    elif(peso < menor or menor == 0):
        menor = peso
    else:
        continue

print("O maior peso é {}kg e o menor é {}kg".format(maior,menor))	
