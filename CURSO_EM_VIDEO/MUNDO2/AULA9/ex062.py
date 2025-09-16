a_zero = int(input("Digite o primeiro termo da PA (ou digite 0 para sair): "))
r = int(input("Digite a razão da PA: "))
i_aux = 10

for i in range(0,10):
    print("a{} = {}".format(i,a_zero + r*i))
    print("PA finalizada.")

opcao = 1
while(opcao != 0):   
    print("Deseja ver mais termos dessa PA? (0 para sair, 1 para continuar)")
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        for i in range(i_aux, i_aux + 10):
            print("a{} = {}".format(i,a_zero + r*i))
        i_aux += 10
    elif opcao == 0:
        print("PA finalizada.")