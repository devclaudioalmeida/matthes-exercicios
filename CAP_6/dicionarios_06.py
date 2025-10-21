#Exercício 6.8

pets = []
pet_01 = {'tipo': 'Gato', 'dono': 'Mariana'}
pet_02 = {'tipo': 'Cachorro', 'dono': 'Manoel'}
pet_03 = {'tipo': 'Calopsita', 'dono': 'Ana'}
pet_04 = {'tipo': 'Ramster', 'dono': 'Luiz'}
pet_05 = {'tipo': 'Papagaio', 'dono': 'Fabiano'}
pets.append(pet_01)
pets.append(pet_02)
pets.append(pet_03)
pets.append(pet_04)
pets.append(pet_05)
print('=' * 50)
for pet in pets:
    print(f'{pet['dono']} tem {pet['tipo']}')
print('=' * 50)