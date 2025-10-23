#Exercício 7.3 É multiplo de 10?

numero = int(input('Por favor digite um número: '))
if (numero % 10) == 0:
    print(f'O número {numero} é multiplo de 10!')
else:
    print(f'O número {numero} não é multiplo de 10!')