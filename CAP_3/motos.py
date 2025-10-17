#praticando os métodos para trabalhar com listas
motos = ['honda', 'yamaha', 'suzuki']
#inserindo elementos em uma lista
print(motos)
motos.append('bmw')#adiciona o elemento 'bmw' ao final da lista
print(motos)
motos.insert(1, 'ducati')
print(motos)#adiciona 'ducati' no indice 1 da lista, ou seja, na segunda posição
#removendo elementos de uma lista
del motos[0]#remove o primeiro elemento da lista motos, no caso aqui: 'honda'
print(motos)
popped_motos = list()
popped_motos.append(motos.pop())#remove o ultimo elemento da lista motos e insere em uma nova lsta popped_motos
print(motos)
print(popped_motos)
popped_motos.append(motos.pop(1))#remove o segundo elemento da lista motos no caso, 'yamaha' e insere em uma nova lsta popped_motos
print(motos)
print(popped_motos)
removed_motos = list()
motos.remove('suzuki')#remove o elemento 'suzuki' da lista motos
print(f'lista motos: {motos}')
print(f'lista motos "poppadas": {popped_motos}')