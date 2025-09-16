frase = input('Digite uma frase: ')

print('A letra A aparece {} vezes na frase.'.format(frase.upper().count('A')))

print("Ela aparece a primeira vez na posição {} e pela ultima vez na posição {}".format(frase.upper().find('A') + 1, frase.upper().rfind('A') + 1))