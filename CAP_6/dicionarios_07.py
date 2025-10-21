#Exercício 6.9

lugares_favoritos = {
    'Claudio': 'Florianópolis', 
    'Maira' : 'Gramado',
    'Manoela' : 'Roma',
    'Tiago' : 'Suécia'
}
print('=' * 50)
for pessoa, lugar in lugares_favoritos.items():
    print(f'Lugar favorito de {pessoa} é {lugar}!')
print('=' * 50)
