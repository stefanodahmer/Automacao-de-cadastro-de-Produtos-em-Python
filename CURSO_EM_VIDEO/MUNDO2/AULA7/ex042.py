
ano = int(input("Digite o ano de nascimento: "))
categoria = 2025 - ano

if(0 < categoria <= 9):
	print("Categoria \033[1;31mMIRIM\033[m");
elif(9 < categoria <= 14):
	print("Categoria \033[1;31mINFANTIL\033[m");
elif(13 < categoria <= 19):
	print("Categoria \033[1;31mJUNIOR\033[m");
elif(19 < categoria <= 20):
	print("Categoria \033[1;31mSÊNIOR\033[m");
elif(categoria>20):
	print("Categoria \033[1;31mMASTER\033[m");
else:
	print("Insira um ano válido")