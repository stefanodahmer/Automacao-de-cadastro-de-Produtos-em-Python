altura = float(input("Insira sua altura em metros: "))
peso = float(input("Insira seu peso: "))

imc = peso / (altura**2)

if(0 < imc < 18.5):
	print("Você está \033[1;31mABAIXO\033[m do peso")
elif(18.5 < imc <= 25):
	print("Você está no peso \033[1;32mIDEAL\033[m")
elif(25 < imc <= 30):
	print("Você está \033[1;31mSOBREPESO\033[m")
elif(30 < imc <= 40):
	print("Você está \033[1;31mOBESO\033[m")
elif(imc>40):
	print("Você está \033[1;31mMUITO GORDAO PQP\033[m")
else:
	print("Insira dados válidos")