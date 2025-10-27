
from CAP_8.funcoes_01 import livro_favorito
from CAP_9.classes_03 import *


def test_livro_favorito():
    """Teste da função livro favorito"""
    livro = livro_favorito('Curso Intensivo de Python')
    assert livro == 'Curso Intensivo de Python'

def test_cadastro_carro_eletrico():
    meu_carro = CarroEletrico('BYD', 'Dolphin', '2024')
    meu_carro.bateria.get_autonomia()
    meu_carro.bateria.troca_bateria()
    meu_carro.bateria.get_autonomia()
    assert 'BYD' in meu_carro.marca