n = 0
lista = []
for i in range(0,5):
    n = int(input("Digite o {}º número: ".format(i+1)))
    lista.append(n)

print("O maior número é {} e está na(s) posição(ões): ".format(max(lista)), end="")
for i, v in enumerate(lista):
    if v == max(lista):
        print(i, end="... ")

print("\nO menor número é {} e está na(s) posição(ões): ".format(min(lista)), end="")
for i, v in enumerate(lista):
    if v == min(lista):
        print(i, end="... ")