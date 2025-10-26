#Solução exercícios 10.11 e 10.12

from pathlib import Path
import json

def cadastra_numero(mensagem, caminho):
    """Cadastra um número em um arquivoo .json"""
    cam = Path(caminho)
    num = input(mensagem)
    conteudo = json.dumps(num)
    cam.write_text(conteudo)
    

def ler_numero(caminho):
    cam = Path(caminho)
    if cam.exists():
        conteudo = cam.read_text()
        num = json.loads(conteudo)
        return num
    else:
        return None


#cadastra_numero('Por favor digite seu numero favorito:  ', '/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/numro_favorito.json')
#print(f'Eu sei que seu número favorito é: {ler_numero('/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/numro_favorito.json')}')