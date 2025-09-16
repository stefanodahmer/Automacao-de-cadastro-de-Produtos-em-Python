
soma = 0
qnt_numeros = 0
res = "S"
maior = 0
menor = 0

while res == "S":
    n = int(input('Digite um número: '))
    soma = soma + n
    qnt_numeros += 1
    if(n > maior):
        maior = n
    if(menor == 0):
        menor = n
    if(n < menor):
        menor = n
    res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    
media = soma / qnt_numeros
print(f'Você digitou {qnt_numeros} números e a média foi {media:.2f}, o menor valor foi {menor} e o maior foi {maior}.')




