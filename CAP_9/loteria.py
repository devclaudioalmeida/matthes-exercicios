from random import choice

class Loteria:
    def __init__(self):
        #Atribui os numeros disponívesi para sorteio
        self.num = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    def bilhete_premiado(self):
        bilhete = []
        for i in range(0, 4):
            bilhete.append(choice(self.num))
        return bilhete
    
lot = Loteria()
#bil = lot.bilhete_premiado()
bil = []
meu_bilhete = ['1', '2', '3', '4']
cont = 0
while bil != meu_bilhete:
    bil = lot.bilhete_premiado()
    cont += 1
print(f'Foram feitos {cont} sorteios até meu bilhete ser sorteado!')