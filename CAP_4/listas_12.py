#Exercício 4.12
my_pizzas = ['frango', 'calabresa', 'muzzarela']
friend_pizzas = my_pizzas[:]
my_pizzas.append('tomate')
friend_pizzas.append('pepeone')
for my_pizza in my_pizzas:
    print(f'Minha pizza favorita: {my_pizza}')
for friend_pizza in friend_pizzas:
    print(f'Pizza favorita do meu amigo: {friend_pizza}')