num = int(input("Digite um número: "))

if num < 2:
    print(f"{num} não é primo")
else:
    eh_primo = True
    for i in range(2, int(num ** 0.5) + 1):  # só vai até a raiz quadrada
        if num % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"{num} é primo")
    else:
        print(f"{num} não é primo")
