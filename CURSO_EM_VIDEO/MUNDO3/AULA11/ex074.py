import random

n1 = random.randint(0,10)
n2 = random.randint(0,10)   
n3 = random.randint(0,10)
n4 = random.randint(0,10)   
n5 = random.randint(0,10)

tupla = (n1, n2, n3, n4, n5)

print("Os números sorteados foram: ", end='')
for n in tupla:
    print(f"{n} ", end='')

maior = max(tupla)
menor = min(tupla)

print(f"\nO maior valor sorteado foi {maior}")
print(f"O menor valor sorteado foi {menor}")