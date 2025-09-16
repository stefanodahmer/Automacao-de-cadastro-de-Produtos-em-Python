
def tabuada(x):
    for i in range (1,11):
        mul = x*i
        print('{} x {} = {}\n'.format(x,i,mul))

n = int(input('Digite um valor para er calculcado a tabuada: '))

tabuada(n)

