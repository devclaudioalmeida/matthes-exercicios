#Exercício 7.4 Ingredientes de uma pizza

print(('=' * 60))
print('PIZZARIA DELICIAS MINEIRAS')
print(('=' * 60))
ingrediente = str(input('Informe o primeiro ingrediente da sua pizza ou "sair" para encerrar! '))
while True:
    if ingrediente.lower().strip() == 'sair':
        print('\nSua pizza será preparada agora.\nObrigado pelo pedido!')
        break
    print(f'Adicionando {ingrediente}...\n')
    ingrediente = str(input('Informe o proximo ingrediente ou "sair" para encerrar! '))