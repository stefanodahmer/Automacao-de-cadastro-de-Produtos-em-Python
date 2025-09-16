n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

noves = 0
pares = []
first_i = -1

numeros = (n1, n2, n3, n4)

for i, n in enumerate(numeros, start=1):  # enumerate dá (posição, valor)
    if n == 9:
        noves += 1
    if n == 3:
        if first_i == -1:
            first_i = i 

    if n % 2 == 0:
        pares.append(n)

print(f"O número 9 apareceu {noves} vezes.")
print(f"Os números pares são: {pares}")

if first_i != -1:
    print(f"O número 3 apareceu pela primeira vez na posição {first_i}.")
else:
    print("O número 3 não foi digitado.")
