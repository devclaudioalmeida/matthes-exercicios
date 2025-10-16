name = '     adA loveLAce     '
print(name.title())
print(name.title().strip())
print(name.title().rstrip())
print(name.title().lstrip())
print(name.upper())
print(name.lower())
first_name = 'ada' 
last_name = 'lovelace'
full_name = f'O seu nome completo é: {first_name.title()} {last_name.title()}'
print(full_name)
url = 'https://claudioalmeida.com.br'
print(f'Url do site completa: {url}')
print(f'Url curta do site: {url.removeprefix('https://')}')