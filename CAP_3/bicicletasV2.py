#Exibe no console uma string contendo a lista bicicletas
#Agora já trabalhando o laço for e algumas técnicas para trabalhar com os elementos da lista
bicicletas = ['OX Bike', 'GTS', 'Sundown', 'TSW', 'Caloi', 'Monark']
print(f'Lista de marcas de bicicletas = {bicicletas}')
print('Marcas de bikes: ', end = ' ')
for i in range (0, len(bicicletas)):
    print(bicicletas[-(i+1)], end = ', ' if (i < len(bicicletas)-1) else '')#Imprime os elementos da lista em ordem inversa
print(' e acabou!')
print(bicicletas[-2])#Secolocar o indice [-1] na lista sempre será acessado o último elemento