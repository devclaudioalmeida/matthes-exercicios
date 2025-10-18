#Continuando com as práticas de listas fatiamento e cópis de listas
my_foods = ['arroz', 'feijão', 'carne', 'frango', 'alface']
friend_foods = my_foods[:] # Se fazer assim gera somente uma cópia da lista
#friend_foods = my_foods # Se fazer assim cria um link entre as duas listas
print(f'Minhas comidas favoritas: {my_foods}')
print(f'Comidas favoritas do meu amigo: {friend_foods}')
friend_foods.append('churrasco')
friend_foods.append('sorvete')
friend_foods.append('chocolate')
print(f'Minhas comidas favoritas: {my_foods}')
print(f'Comidas favoritas do meu amigo atualizada: {friend_foods}')