#Exercício 7.5 Ingressos de cinema flag de parada

ativo = True
while ativo:
    print('=' * 50)
    print('CINEMA DA CIDADE')
    print('Consulta de valor do ingresso')
    print('=' * 50)
    idade = int(input('Informe sua idade de 0 a 99 anos: '))
    if idade < 0:
        print('ERRO! idade inválida, por favor tente novamente!')
    elif idade <= 3:
        print(f'Para pessoas de {idade} anos a entrada é franca!')
    elif idade <= 12:
        print(f'Para pessoas de {idade} anos o ingresso custa R$ 10,00')
    elif idade <= 99:
        print(f'Para pessoas de {idade} anos o ingresso custa R$ 15,00')
    else:
        print('Finalizando...')
        print('Obrigado por usar o programa.')
        print('Volte Sempre!')
        ativo = False