somatorio = 0

for i in range(1, 501):
	
    if(i%3 == 0 and i%2 == 1):
        somatorio = somatorio  + i
    else:
        continue

print("FIM. O somatório foi de {}".format(somatorio))