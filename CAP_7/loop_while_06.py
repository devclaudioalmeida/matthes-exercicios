#Exercício 7.9 Lanchonete (sem pastrami)

print('=' * 50)
print('LANCHONETE KI-LANCHE')
print('=' * 50)
sandwich_orders = ['X-Tudo', 'X-Bacon', 'Pastrami', 'X-Salada', 'Pastrami',
    'X-Egg-Bacon', 'Pastrami', 'Cachorro-Quente', 'Pastrami',
    ]
finished_sandwichs = []
print(f'{sandwich_orders}')
if 'Pastrami' in sandwich_orders:
    print('Desculpe, a lanchonete está sem Pastrami, por isso tosos os pedidos com Pastrami serão cancelados!')
    print('=' * 50)
    while 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')
sandwich_orders.reverse()
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwichs.append(sandwich)
    print(f'Seu {sandwich} está pronto!')
print('=' * 50)
for num, sandwich in enumerate(finished_sandwichs):
    print(f'{num + 1}. {sandwich}')