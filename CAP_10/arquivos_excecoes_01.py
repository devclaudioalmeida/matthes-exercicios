#Resolução exercícios 10.4, 10.5, 10.8, 10.9, 10.10

from pathlib import Path

def escrever_arquivo(mensagem, caminho):
    texto = ''
    while True:
        txt = input(mensagem)
        
        if txt.lower().strip() == 'q':
            break
        texto += txt + '\n'
    path = Path(caminho)
    path.write_text(texto)

def ler_arquivo(caminho):
    path = Path(caminho)
    try:
        conteudo = path.read_text()
    except FileNotFoundError:
        pass
        #print('Desculpe, mas não consegui localizar o arquivo!')
        
    else:
        print(conteudo)

def conta_palavras (palavra, caminho):
    cont = 0
    path = Path(caminho)
    try:
        conteudo = path.read_text()
    except FileNotFoundError:
        pass
        #print('Desculpe, mas não consegui localizar o arquivo!')
        
    else:
        cont = conteudo.lower().count(palavra.lower())
        print(f'Este texto contem {cont} palavras "{palavra}"!')



#print('+' * 60)
#escrever_arquivo('/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/gatos.txt')
#print('+' * 60)
#escrever_arquivo('/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/cachorros.txt')
#print('+' * 60)
#ler_arquivo('/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/gatos.txt')
#print('+' * 60)
#ler_arquivo('/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/cachorros.txt')
#print('+' * 60)
#print('+' * 60)
#escrever_arquivo('Por favor digite o nome do convidado ou "q" para sair: ', '/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/lista_convidados.txt')
#escrever_arquivo('Por favor digite o nome do convidado ou "q" para sair: ', '/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/texto.txt')
#ler_arquivo('/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/texto.txt')
#print('+' * 60)
#conta_palavras('Mexer', '/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/texto.txt')