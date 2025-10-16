name = '     clAUdio aLmEiDa    '
print(name.title())
print(name.title().strip())
print(name.title().rstrip())
print(name.title().lstrip())
print(name.upper())
print(name.lower())
first_name = 'claudio' 
last_name = 'almeida'
full_name = f'O seu nome completo é: {first_name.title()} {last_name.title()}'
print(full_name)
url = 'https://claudioalmeida.com.br'
print(f'Url do site completa: {url}')
print(f'Url curta do site: {url.removeprefix('https://')}') #remove o prefixo 'https://'
arq = 'teste.txt'
print(f'Nome do arquivo com extensão: {arq}')
print(f'Nome do arquivo sem extensão: {arq.removesuffix('.txt')}') # Remove o sufixo '.txt'
n = 14_000_000 #pode usar o underline(_) para separador de milhar em python pois ele é ignorado na atribuição, que interessante 
print(n)
x, y, z = 1, 2, 3 #atribuição múltipla
print(f'x = {x}, y = {y} e z = {z}' )
CONSTANTE = 10 #Programadores de Python declaram constantes em letras maiúsculas
print(CONSTANTE)
