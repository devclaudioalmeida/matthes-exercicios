#Resolução exercícios 10.13 e 10.14

from pathlib import Path
import json

def cadastra_usuario(caminho):
    """Faz o cadastro das informações do usuário em um dicionário"""
    cam = Path(caminho)
    cad = {}
    cad['nome'] = input('Digite seu nome')
    cad['sexo'] = input('Sexo [M / F]')
    cad['idade'] = input('Idade:')
    cadastro = json.dumps(cad)
    cam.write_text(cadastro)

def ler_usuario(caminho):
    """Le um dicionario com as informações de usuário"""
    cam = Path(caminho)
    if cam.exists():
        content = cam.read_text()
        info = json.loads(content)
        return info
    else:
        return None
    

#cadastra_usuario('/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/user.json')
#print(f'Informações do usuário: {ler_usuario('/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/user.json')}')
