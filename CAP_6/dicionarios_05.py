#Exercício 6.7

pessoas = []
pessoa_01 = {'Primeiro nome': 'José', 'Ultimo nome': 'Almeida', 'Idade' : '58', 'Cidade': 'Blumennau'}
pessoa_02 = {'Primeiro nome': 'Maria', 'Ultimo nome': 'Souza', 'Idade' : '47', 'Cidade': 'Manaus'}
pessoa_03 = {'Primeiro nome': 'Aldo', 'Ultimo nome': 'Santos', 'Idade' : '43', 'Cidade': 'Campinas'}
pessoas.append(pessoa_01)
pessoas.append(pessoa_02)
pessoas.append(pessoa_03)
for pes in pessoas:
    print(f'\nPrimeiro nome: {pes['Primeiro nome']}')
    print(f'Último nome: {pes['Ultimo nome']}')
    print(f'Idade: {pes['Idade']}')
    print(f'Mora em: {pes['Cidade']}')
