listagem = ('Lápis',1.75,
            'Borracha',2.00,
            'Caderno',15.90,
            'Estojo',25.00,)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:.<30} R$ {listagem[i+1]:>7.2f}')
print('-'*40)
