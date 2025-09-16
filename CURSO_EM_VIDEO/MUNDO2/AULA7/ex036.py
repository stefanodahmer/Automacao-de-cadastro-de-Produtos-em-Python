valor = float(input('Digite o valor do casa: R$ '))

salario = float(input('Digite o salário do funcionário: R$ '))

anos = int(input("Informe em quantos anos o valor será pago:"))

prestacao = valor / (anos * 12)

if(prestacao >= 0.3*salario):
    print('Empréstimo \033[1;31mNEGADO\033[m! A prestação de \033[1;32mR${:.2f}\033[m excede 30% do salário.'.format(prestacao))
else: 
    print('Empréstimo \033[1;32mAPROVADO\033[m! A prestação será de \033[1;32mR${:.2f}\033[m.'.format(prestacao))
