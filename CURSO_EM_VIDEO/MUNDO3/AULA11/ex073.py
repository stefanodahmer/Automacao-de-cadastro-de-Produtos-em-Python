times = ("Flamengo", "Palmeiras", "Cruzeiro", "Mirassol", "Bahia", "Botafogo", "São Paulo", "Bragantino", "Fluminense", "Internacional", "Corinthians", "Ceará", "Grêmio", "Atlético-MG", "Vasco", "Santos", "Vitória", "Juventude", "Fortaleza", "Sport")

print("TOP 5 times do Brasileirão: ")

for i in range (0,5):
    print(f"{i+1}º - {times[i]}")

print("\nOs 4 últimos colocados são: ")
for i in range(len(times)-4, len(times)):
    print(f"{i+1}º - {times[i]}")

print("\nTimes em ordem alfabética: ")
print(sorted(times))

if "Vasco" in times:
    print(f"\nO Vasco está na {times.index('Vasco')+1}ª posição")