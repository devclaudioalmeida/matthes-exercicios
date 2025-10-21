#Exercícios 5.8 e 5.9
#5.8 Lista de usuáris com mensagens especial para o admin
#5.9 tratamento da lista vasia de usuários

usuarios = ['pedro', 'maria', 'admin', 'marcos']
#usuarios = []
if usuarios:
    for usuario in usuarios:
        if usuario.lower() == 'admin':
            print('Seja bem vindo administrador, deseja obter os relatórios?')
        else:
            print(f'Seja bem vindo {usuario}!')
else:
    print('ERRO! não foram encontrados usuários no sistema!')