ano = int(input("Digite o ano de nascimento: "))
ano_aux = 0

if(2025-ano<18):
    ano_aux = 18 - (2025-ano)
    print("Você ainda vai se alistar ao serviço militar. Faltam \033[1;32m{}\033[m anos.".format(ano_aux))
elif(2025-ano==18):
    print("Você deve se alistar ao serviço militar \033[1;31mIMEDIATAMENTE\033[m!")
else:
    print("Você já deveria ter se alistado ao serviço militar. Já se passaram {} anos.".format((2025-ano)-18))