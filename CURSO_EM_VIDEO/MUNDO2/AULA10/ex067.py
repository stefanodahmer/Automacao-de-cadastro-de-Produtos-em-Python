n = 1

while n > 0:
    n = int(input('Digite um número para a tabuada: '))
    
    for c in range(1, 11):
        if n > 0:
            print(f'{n} x {c} = {n*c}')
    
print('Programa de tabuada encerrado. Volte sempre!')