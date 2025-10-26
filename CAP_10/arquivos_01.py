#Começando a trabalhar com arquivos

from pathlib import Path

path = Path('/home/claudio/Documentos/Meus_Projetos/Python/matthes-exercicios/CAP_10/aprendendo_python.txt')
conteudo = path.read_text()
print('~' *80)
for linha in conteudo.splitlines():
    print(linha)
print('~' *80)
path.write_text('Estou aprendendo Python!')
for linha in conteudo.splitlines():
    print(linha)