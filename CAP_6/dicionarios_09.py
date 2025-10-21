#Exercício 6.11

cidades = {
    'Congonhas':{
        'populacao': 50000,
        'país': 'Brasil',
        'fato': "Cidade das obras barrocas de alejadinho."
    },
    'Cons Lafaiete': {
        'populacao': 80000,
        'país': 'Brasil',
        'fato': "Cidade com o comércio muito forte."
    },
    'Belo Horizonte': {
        'populacao': 250000,
        'país': 'Brasil',
        'fato': "Capital de Minas Gerais."
    }
}

for cidade, info in cidades.items():
    print(f'\nCidade: {cidade}')
    print(f'População: {info['populacao']}')
    print(f'País: {info['país']}')
    print(f'Detalhes: {info['fato']}')