import math

co = float(input("Insira o valor do cateto oposto: "))
ca = float(input("Insira o valor do cateto adacente: "))

hip = math.sqrt((co**2)+(ca**2))


print('O valor da hipotenusa é {}'.format(hip))