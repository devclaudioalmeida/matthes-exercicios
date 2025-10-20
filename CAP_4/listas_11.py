#Exercício 4.11
my_pizzas = ['frango', 'calabresa', 'muzzarela']
friend_pizzas = my_pizzas[:]
print(f'Minhas pizzas favoritas são: {my_pizzas}')
print(f'As pizzas favoritas do meu amigo são: {friend_pizzas}')
my_pizzas.append('tomate')
friend_pizzas.append('pepeone')
print(f'Minhas pizzas favoritas agora são: {my_pizzas}')
print(f'As pizzas favoritas do meu amigo agora são: {friend_pizzas}')