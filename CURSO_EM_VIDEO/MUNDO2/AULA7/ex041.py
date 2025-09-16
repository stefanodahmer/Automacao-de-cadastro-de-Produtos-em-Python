n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1+n2) / 2

if(media>=7.0):
	print("Parábens você foi \033[1;32mAPROVADO\033[m!")
elif(5.0 <= media < 7.0):	
	print("Você ficou de \033[1;31mRECUPERAÇÃO\033[m!")
else:
	print("Você foi \033[1;31mREPROVADO\033[m!")