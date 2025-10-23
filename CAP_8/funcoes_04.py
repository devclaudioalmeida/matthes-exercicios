#Exercício 8.12

def sandwiches (*ingredientes):
    """Exibe os ingredietes que serão osados para fazer o sanduiche"""
    print('Seu sanduiche será feito com os seguintes infredientes:')
    for ingrediente in ingredientes:
        print(f' - {ingrediente}')


