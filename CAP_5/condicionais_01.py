#Exercício 5.1 e 5.2 Testes condicionais.
car = 'BMW'
print(f'Eu amo {car}!'if car.lower() == 'bmw' else f'Eu não gosto muito de {car}!')
print(car.lower() == 'bmw')
lista_carros = ['BMW', 'Audi', 'Mercedes', 'Jaguar', 'Ford']
for carro in lista_carros:
    if carro.lower() == 'mercedes':
        print(f'{carro} está na minha lista de carros favoritos!')
    else:
        print(f'{carro} são legais!')
if len(lista_carros) > 4:
    print(f'Minha lista de carros está legal com tamanho {len(lista_carros)}!')
else:
    print(f'Minha lista está com tamanho {len(lista_carros)}, preciso adicionar mais!')

favorito = 'BMW'
if len(lista_carros) > 6 or favorito.lower() == 'bmw':
    print(f'Minha lista de carros está legal com tamanho {len(lista_carros)} ou tem a marca {favorito}!')
else:
    print(f'Minha lista está com tamanho {len(lista_carros)}, preciso adicionar mais e tenho que acicionar a marca {favorito}!')
if 'chevrolet' not in lista_carros:
    print('Falta adiocionar a marca "Chevrolet" na lista de carros')