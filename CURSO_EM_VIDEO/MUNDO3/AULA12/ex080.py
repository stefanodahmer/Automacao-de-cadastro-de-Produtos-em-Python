lista = []

n1 = int(input("Digite um valor: "))
lista.append(n1)
print("Valor adicionado no final da lista...")

n2 = int(input("Digite um valor: "))
if(n2 < lista[0]):
    lista.insert(0, n2)
    print("Valor adicionado na posição 0 da lista...")
elif(n2 >= lista[-1]):
    lista.append(n2)
    print("Valor adicionado no final da lista...")

n3 = int(input("Digite um valor: "))
for i in range(0, len(lista)):
    if(n3 <= lista[i]):
        lista.insert(i, n3)
        print("Valor adicionado na posição {} da lista...".format(i))
        break
    elif(i == len(lista) - 1):
        lista.append(n3)
        print("Valor adicionado no final da lista...")

n4 = int(input("Digite um valor: "))
for i in range(0, len(lista)):
    if(n4 <= lista[i]):
        lista.insert(i, n4)
        print("Valor adicionado na posição {} da lista...".format(i))
        break
    elif(i == len(lista) - 1):
        lista.append(n4)
        print("Valor adicionado no final da lista...")

n5 = int(input("Digite um valor: "))
for i in range(0, len(lista)):
    if(n5 <= lista[i]):
        lista.insert(i, n5)
        print("Valor adicionado na posição {} da lista...".format(i))
        break
    elif(i == len(lista) - 1):
        lista.append(n5)
        print("Valor adicionado no final da lista...")

print("Os valores digitados em ordem foram {}".format(lista))

