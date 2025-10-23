#Exercícios 8.1 , 8.2, 8.3, 8.4, 8.5


def mostrar_mensagem():
    """Exibe uma simples mensagem na tela"""
    print('Olá estou aprendendo Python!')

def livro_favorito(livro):
    """Exibe uma mensagem na tela com o livro favorito"""
    print(f'Meu livro favorito é: {livro}')

def make_shirt(tam='G', texto='Eu amo Python!'):
    """
    Exibe o tamnho da camiseta e a frase que será estampada nela
    o tamanho pagrão é 'G' e a mensagem padrão é 'Eu amo Python!'
    """
    print(f'Será confeccionada uma camiseta tamanho "{tam}" com a frase "{texto}" estampada nela!')

def descreva_cidade(cidade='Florianópolis', pais='Brasil'):
    """Exibe o nome de uma cidade e em qual pais ela está localizada!"""
    print(f'{cidade} está localizada no(a) {pais}!')


mostrar_mensagem()
print('=' * 50)
fav_livro = 'Curso Intensivo de Python'
livro_favorito(fav_livro)
print('=' * 50)
make_shirt(texto='Sou de mais!', tam='M')
make_shirt('XG', 'Eu não sou GORDO!')
make_shirt('P')
make_shirt(texto='Simplesmente de mais!')
make_shirt()
print('=' * 50)
descreva_cidade(cidade='Belo Horizonte')
descreva_cidade(pais='Itália', cidade='Veneza')
descreva_cidade()
print('=' * 50)