#Exercício 7.10 Ferias tão sonhadas

respostas = {}
print('=' * 60)
print('PESQUISA VIAGEM DOS SONHOS')
print('=' * 60)
while True:
    #Solicia o nome do usuário
    nome = str(input('Digite seu nome: '))
    resposta = str(input('Que lugar voce gostaria de visitar? '))

    #Armazena as respostas em um dicionário
    respostas[nome] = resposta

    continua_pesquisa = str(input('Deseja continuar a pesquisa [S/N]?'))
    if continua_pesquisa.upper().strip() == 'N':
        print('=' * 60)
        print('Pesquisa finalizada!')
        print('Exibindo resultados...')
        print('=' * 60)
        break
#mosta todasas respostas após a pesquisa ser finalizada
for nome, resposta in respostas.items():
    print(f'{nome} gostaria de visitar {resposta}')
print('=' * 60)