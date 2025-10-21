#Exercícios 5.3, 5.4 e 5.5
#Exercício 5.3 somente if
#Exercício 5.4 uso de if e else
#Exercício 5.5 uso de if elif e else

alien_color = 'Verde'
if alien_color.lower() == 'verde':
    print('O jogador acaba de ganhar 5 pontos!')
elif alien_color.lower() == 'amarelo':
    print('O jogador acaba de ganhar 10 pontos!')
elif alien_color.lower() == 'vermelho':
    print('O jogador acaba de ganhar 15 pontos!')
else:
    print('Houve algum erro!')