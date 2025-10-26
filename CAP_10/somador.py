#Uma simples calculadora de somas para os exercícios 10.6 e 10.7

def somador ():
    
    while True:
        print('=' * 50)
        print('Insira dois numeros e eu vou somá-los pra voce!')
        print('A hora que quiser encerrar digite "q"')
        print('=' * 50)
        #Começa a receber os números e se for digitado "q" sai do programa
        n1 = input('Digite o primeiro número:')
        if n1.lower().strip() == 'q':
            break
        n2 = input('Digite o segundo número: ')
        if n2.lower().strip() == 'q':
            break
        print('=' * 50)
        try:
            n1 = int(n1)
            n2 = int(n2)
        except ValueError:
            print('Por favor insira somente números ou "q" para sair!')
        else:
            print(f'O resultado da soma é: {n1 + n2}')


somador()