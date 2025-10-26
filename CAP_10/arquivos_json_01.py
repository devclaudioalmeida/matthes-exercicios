from pathlib import Path
import json

def cadastra_numero(mensagem, caminho):
    """Cadastra um número em um arquivoo .json"""
    #cam = Path(caminho)
    num = input(mensagem)
    conteudo = json.dumps(num)
    caminho.write_text(conteudo)
    

def ler_numero(caminho):
    if caminho.exists():
        conteudo = caminho.read_text()
        num = json.loads(conteudo)
        return num
    else:
        return None


caminho = Path('/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/numro_favorito.json')
#cadastra_numero('Por favor digite seu numero favorito:  ', caminho)
print(f'Eu sei que seu número favorito é: {ler_numero(caminho)}')