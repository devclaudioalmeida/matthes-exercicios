#Testes práticos de fatiamento de lista
pizzas = ['calabresa', 'queijo', 'bolonhesa', 'atum', 'peperone','frango', 'bacon']
print(pizzas[0:3])
print(pizzas[1:4])
print(pizzas[:2])
print(pizzas[2:])
print(pizzas[-2:])
print(pizzas[:-3])
print(pizzas[0:5:2])
print()
print('Mostra as 3 primeiras pizzas!')
for pizza in pizzas[:3]: #Vai do inicio até o terceiro elemento
    print(pizza)
print()
print('Mostra as 3 ultimas pizzas!')
for pizza in pizzas[-3:]: #começa do antepenultomo até o ultimo
    print(pizza)
print()
print('Mostra as 3 pizzas no meio da lista!')
for pizza in pizzas[2:5]: #vali do terceiro elemento até o quinto
    print(pizza)