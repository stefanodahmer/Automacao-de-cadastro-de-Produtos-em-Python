count = 0

for i in range(1,8):
    ano = int(input("Digite o {}° ano de nascimento: ".format(i)))

    if(2025-ano >= 21):
        count = count + 1
    else:
        continue

print("Ao todo {} pessoas são maiores de idade e {} são menores de idade.".format(count, 7 - count))
