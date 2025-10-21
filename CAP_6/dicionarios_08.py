#Exercício 6.10

num_favoritos = {
    'Claudio': [2 ,3],
    'Manoel':[],
    'Jessica': [1],
    'Marina': [3, 4, 5]
}
print('=' * 60)
for p, n in num_favoritos.items():
    if not n:
        print(f'\n{p} não possui números favoritos!', end='')
    elif len(n) == 1:
        print(f'\nO numero favorito de {p} é: ', end='')
        for num in n:
            print(num, end=' ')
    else:
        print(f'\nOs numeros favoritos de {p} são: ', end='')
        for num in n:
            print(num, end=' ')
print('\n')
print('=' * 60)