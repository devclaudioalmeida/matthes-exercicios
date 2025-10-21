#Exercício 6.6

linguagens_preferidas = {
    'jem': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phill': 'python'
}
pessoas_pesquisas = ['lucy', 'jeremy', 'jem', 'sarah', 'doug', 'edward', 'phill']
for pessoa in pessoas_pesquisas:
    if pessoa in linguagens_preferidas.keys():
        print(f'Obrigado {pessoa.title()} por ter respondido a pesquisa!')
    else:
        print(f'Por favor {pessoa.title()}, responda a pesquisa!')