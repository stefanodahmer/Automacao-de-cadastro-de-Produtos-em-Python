n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))


def media(x,y):
    return (x+y) /2

def aprovado(x) :
    if x>=6.0 :
        return "Aprovado"
    else:
        return "Reprovado"

print('Sua média foi de: {}. Você foi {}'.format(media(n1,n2), aprovado((media(n1,n2)))))
