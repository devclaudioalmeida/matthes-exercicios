#Exercício 7.6 Ingredientes de uma pizza teste no while para saida

print(('=' * 60))
print('PIZZARIA DELICIAS MINEIRAS')
print(('=' * 60))
ingrediente = str(input('Informe o primeiro ingrediente da sua pizza ou "sair" para encerrar! '))
while ingrediente.lower().strip() != 'sair':    
    print(f'Adicionando {ingrediente}...\n')
    ingrediente = str(input('Informe o proximo ingrediente ou "sair" para encerrar! '))
print('\nSua pizza será preparada agora.\nObrigado pelo pedido!')