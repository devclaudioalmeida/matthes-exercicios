#exercícios 8.6, 8.7 e 8.8

#Função para o exercício 8.6
def city_country(cidade, pais):
    """Retorna uma string formatada com o nome da cidade e o pais de origem"""
    return f'{cidade.title()}, {pais.title()}'

def make_albun(artista, album, nome=None):
    """Retorna um dicionário contendo o nome de um artista e o nome de um albun"""
    if nome:
        alb = {'nome': nome.title(), 'artista': artista.title(), 'albun': album.title()}
    else:
        alb = {'artista': artista.title(), 'albun': album.title()}
    return alb


print('-' * 60)
print(city_country('roma', 'italia'))
print(city_country('moscou', 'russia'))
print(city_country('tokio', 'japao'))
#solução do 8.6 até aqui
print('-' * 60)

#A partir daqui são resolvidos o 8.7 e o 8.8
while True:
    print('por favor insira as informações solicitadas ou q para sair do programa!')
    nome = str(input('Digite seu nome:'))
    if nome.lower() == 'q':
        break
    artista = str(input('Digite o nome do artista:'))
    if artista.lower() == 'q':
        break
    album = str(input('Digite o título do albun:'))
    if album.lower == 'q':
        break

    print(make_albun(artista, album, nome))
    
