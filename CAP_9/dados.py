from random import randint

class Dado:
    """Inicia o atributo lados do dado"""
    def __init__(self):
        self.lados = 6
    
    def jogar_dado(self):
        print(f'O dado parou em {randint(1,6)}!')

dado = Dado()
dado.jogar_dado()