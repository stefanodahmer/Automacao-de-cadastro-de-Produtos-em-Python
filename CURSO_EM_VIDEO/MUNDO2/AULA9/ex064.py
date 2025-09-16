flag = 999
soma = 0
qnt_numeros = 0

n = int(input('Digite um número [999 para parar]: '))

while n != flag:
    soma = soma + n
    qnt_numeros += 1
    n = int(input('Digite um número [999 para parar]: '))
    

print(f'Você digitou {qnt_numeros} números e a soma entre eles foi {soma}.')


