import math
ang = float(input("Digite o valor do ângulo em graus: "))

rad = math.radians(ang)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print("Seno de {}°: {:.2f}\nCosseno de {}°: {:.2f}\nTangente de {}°: {:.2f}".format(ang, seno,ang,cosseno,ang,tangente))
