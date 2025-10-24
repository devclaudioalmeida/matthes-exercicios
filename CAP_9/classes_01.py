#Exercícios 9.1 e 9.2

class Restaurante:

    #método especial que o python chama automaticamente ao instanciar uma classe
    def __init__(self, nome, tipo):
        #Inicializa os atributos nome e tipo
        self.nome = nome
        self.tipo = tipo
    
    def restaurante_info(self):
        #Exibe uma mensagem informando o tipo de cozinha do restaurante
        print(f'O restaurante {self.nome} tem cozinha tipo {self.tipo}')
    
    def restaurante_aberto(self):
        #Exibe uma mensagem informando que o restaurante está aberto
        print(f'O restaurante {self.nome} está aberto!')


rest_arabe = Restaurante('Sabores Internacional', 'Arabe')
rest_arabe.restaurante_info()
rest_arabe.restaurante_aberto()
rest_italiano = Restaurante('Delicias da Nona', 'Italiana')
rest_japones = Restaurante('SUSHITAKARO', 'Japonesa')
rest_mexicano = Restaurante('Arriba Burritos', 'Mexicana')
rest_japones.restaurante_info()
rest_italiano.restaurante_info()
rest_mexicano.restaurante_info()

