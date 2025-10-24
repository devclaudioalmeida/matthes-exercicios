#Exercícios 9.1 e 9.2, 9.4

class Restaurante:

    #método especial que o python chama automaticamente ao instanciar uma classe
    def __init__(self, nome, tipo):
        #Inicializa os atributos nome e tipo
        self.nome = nome
        self.tipo = tipo
        self.num_servidos = 0
    
    def restaurante_info(self):
        #Exibe uma mensagem informando o tipo de cozinha do restaurante
        print(f'O restaurante {self.nome} tem cozinha tipo {self.tipo}')
    
    def restaurante_aberto(self):
        #Exibe uma mensagem informando que o restaurante está aberto
        print(f'O restaurante {self.nome} está aberto!')

    #A partir daqui é a solução do exerrcício 9.4
    def set_num_served(self, numero):
        #Seta o número de pessoas servidas no restaurante
        self.num_servidos = numero

    def incremeta_num_servidos(self, inc):
        #incrementa o número de pessoas servidas no restaurante
        self.num_servidos += inc
    
    def ler_num_servidos(self):
        #le o numero de pessoas servidas no restaurante
        print(f'Foram servidas {self.num_servidos} pessoas no restaurante {self.nome}!')



rest_arabe = Restaurante('Sabores Internacional', 'Arabe')
rest_arabe.restaurante_info()
rest_arabe.restaurante_aberto()
rest_italiano = Restaurante('Delicias da Nona', 'Italiana')
rest_japones = Restaurante('SUSHITAKARO', 'Japonesa')
rest_mexicano = Restaurante('Arriba Burritos', 'Mexicana')
rest_japones.restaurante_info()
rest_italiano.restaurante_info()
rest_mexicano.restaurante_info()
print('+' *60)
rest_japones.ler_num_servidos()
rest_japones.num_servidos = 1
rest_japones.ler_num_servidos()
rest_japones.set_num_served(3)
rest_japones.ler_num_servidos()
rest_japones.incremeta_num_servidos(2)
rest_japones.ler_num_servidos()