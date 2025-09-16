a_zero = int(input("Digite o primeiro termo da PA (ou digite 0 para sair): "))
r = int(input("Digite a razão da PA: "))

while(True):
    for i in range(0,10):
        print("a{} = {}".format(i,a_zero + r*i))
    
    print("PA finalizada.")
    a_zero = int(input("Digite o primeiro termo da PA (ou digite 0 para sair): "))
    if(a_zero == 0):
        break
    r = int(input("Digite a razão da PA: "))
	