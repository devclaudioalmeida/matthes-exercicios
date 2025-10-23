#Exercício 7.2 Reserva de mesa

mesa = input('Deseja uma mesa de quantos lugares? ')
mesa = int(mesa)
if mesa > 8:
    print(f'Desculpe será necessario aguardar desocupar uma mesa de {mesa} lugares!')
elif mesa < 0:
    print(f'ERRO! Não existe mesa de {mesa} lugares!')
else:
    print(f'Uma mesa com {mesa} lugares já está disponível!')