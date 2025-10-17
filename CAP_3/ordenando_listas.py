#Ordenando listas
carros = list()
carros.append('bmw')
carros.append('audi')
carros.append('toyota')
carros.append('subaru')
print(f'Lista original: {carros}')
carros.sort()#ordena em ordem alfabética, o meto sor ordena a lista permanentemente.
print(f'Lista ordenada com o método sort(): {carros}')
carros.sort(reverse=True)#ordena em ordem alfabética reversa
print(f'Lista ordenada com o método sort(reverse=True): {carros}')
#ordenação temporária
print(f'Lista original atualizada: {carros}')
print(f'Lista ordenada com o método sorted(): {sorted(carros)}')#faz uma ordenação temporária na lista com a função sorted(carros)
print(f'Lista original atualizada: {carros}')
carros.append('chevrolet')
carros.append('hyundai')
carros.append('fiat')
carros.append('kia')
print(f'Lista original atualizada: {carros}')
carros.reverse()
print(f'Lista original atualizada: {carros}')#faz a reversão da lista, nao ordena.
#Identificando o tamanho de uma lista
print(f'O tamanho da lista de carros é: {len(carros)}')
