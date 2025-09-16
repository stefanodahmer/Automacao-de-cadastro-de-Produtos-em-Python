vel = float(input("Digite a velocidade atual do carro: "))
multa = 0

if(vel>80):
    multa = (vel - 80)*7
    print("Você foi multado! O valor da multa é R$ {:.2f}".format(multa))
else:
    print("Tenha um bom dia! Dirija com segurança!")
    
