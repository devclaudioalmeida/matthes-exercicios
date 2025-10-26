from CAP_8.funcoes_01 import livro_favorito

def test_livro_favorito():
    """Teste da função livro favorito"""
    livro = livro_favorito('Curso Intensivo de Python')
    assert livro == 'Curso Intensivo de Python'