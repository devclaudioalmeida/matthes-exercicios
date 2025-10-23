#Exercício 7.8 Lanchonete

print('=' * 50)
print('LANCHONETE KI-LANCHE')
print('=' * 50)
sandwich_orders = ['X-Tudo', 'X-Bacon', 'X-Salada', 'X-Egg-Bacon', 'Cachorro-Quente']
finished_sandwichs = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwichs.append(sandwich)
    print(f'Seu {sandwich} está pronto!')
print('=' * 50)
for num, sandwich in enumerate(finished_sandwichs):
    print(f'{num + 1}. {sandwich}')
