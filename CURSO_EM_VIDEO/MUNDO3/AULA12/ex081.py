n = int(input("Digite um valor: "))
numeros = 1
cincodigitado = False
lista = []

while True:
    res = str(input("Deseja continuar? [S/N]")).upper().strip()[0]

    while res not in "SN":
        res = str(input("Resposta inválida! Deseja continuar? [S/N]")).upper().strip()[0]

    if res == "N":
        print("TCHAU.")
        break

    n = int(input("Digite um valor: "))
    numeros += 1
    lista.append(n)

    if n == 5:
        cincodigitado = True

    lista.sort(reverse=True)


print("Você digitou {} números.".format(numeros))
print("A lista em ordem decrescente é {}".format(lista))



if cincodigitado != False:
    print("O valor cinco foi digitado e esta na posição {}".format(lista.index(5)+1))
else:
    print("O valor cinco não foi digitado")

