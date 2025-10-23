#Exercicio 8.13, 8.14

def build_profile(primeiro, ultimo, **informacoes):
    """
    Cria um perfil de usuário recebendo o primero e o ultimo nome e 
    outros parametros arbitrários que o usuário fornecer
    """
    informacoes['nome'] = primeiro
    informacoes['sobrenome'] = ultimo
    return informacoes


def make_car(fab, mod, **info):
    """
    Cria um cadastro de um carro recebendo o fabricante(fab) e o modelo(mod) como
    parametros obrigatórios, alem de parametros arbitrários que o usuário desejar inserir
    """
    info['fabricante'] = fab
    info['modelo'] = mod
    return info


