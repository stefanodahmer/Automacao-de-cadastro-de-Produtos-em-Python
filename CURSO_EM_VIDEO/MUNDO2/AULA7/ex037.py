n = int(input("Digite um número inteiro: "))

print("Escolha uma base para conversão:  \n1 - Binário\n2 - Octal\n3 - Hexadecimal")
op = int(input("Sua opção: "))
if op == 1:
    print("O número {} em binário é \033[1;34m{}\033[m".format(n, bin(n)[2:]))
elif op == 2:
    print("O número {} em octal é \033[1;34m{}\033[m".format(n, oct(n)[2:]))
elif op == 3:
    print("O número {} em hexadecimal é \033[1;34m{}\033[m".format(n, hex(n)[2:]))
else:
    print("Opção inválida.")