somaidades = 0
maioridade = 0
nomeMaioridade = ""
mulheresmaisdevinte = 0

for i in range(1,5):
    nome = str(input("Digite o {}° nome: ".format(i)))
    idade = int(input("Digite a {}° idade: ".format(i)))
    sexo = str(input("Digite o {}° sexo [M/F]: ".format(i))).upper()

    somaidades = somaidades + idade
    
    if(idade > maioridade and sexo == "M"):
        nomeMaioridade = nome

    if(idade>= 20 and sexo == "F"):
        mulheresmaisdevinte = mulheresmaisdevinte + 1

mediaidades = somaidades / 4

print("Média de idade: {}\nNome do homem mais velho: {}\nMulheres com mais de 20 anos: {}".format(mediaidades, nomeMaioridade, mulheresmaisdevinte))

	


    


