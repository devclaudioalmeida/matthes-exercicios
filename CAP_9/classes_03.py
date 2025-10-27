class Carro:
    def __init__(self, marca, modelo, ano):
        """Inicializa os atributos para descrever um carro"""
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def descreve_carro(self):
        #Retorna a descrição completa do carro
        nome_carro = f'{self.marca} {self.modelo} {self.ano}'
        return nome_carro
    
    def ler_odometro(self):
        #exibe uma mensagem com a quilometragem do carro
        print(f'Este carro tem {self.odometro} km rodados!')
    
    def atualiza_odometro(self, quilometragem):
        #Atualiza o odometro para o valor fornecido
        #Rejeita reversão do odometro
        if quilometragem > self.odometro:
            self.odometro = quilometragem
        else:
            print('Desculpe, mas você nao pode voltar a quilometragem do veículo!')
    
    def incremeta_odometro(self, km):
        self.odometro +=km


class Bateria:
    def __init__(self, capacidade_bateria=40):
        #Inicializa o atributo capacidade da bateria
        self.capacidade_bateria = capacidade_bateria
        
    def descreve_bateria(self):
        #Descreve a capacidade da bateria em KWh
        print(f'Esta bateria tem capacidade de {self.capacidade_bateria} KWh!')
        
    def get_autonomia(self):
        if self.capacidade_bateria == 40:
            aut = 250
        elif self.capacidade_bateria == 65:
            aut = 350
        print(f'Essa bateria completamente carregada tem uma autonomia de até {aut} quilometros!')
    def troca_bateria(self):
        #Metodo para troca da bateria
        while True:
            print('Escola uma das opções de baterias disponíveis:')
            print('1. 40KWh')
            print('2. 65KWh')
            op = int(input('Escolha uma opção: '))
            if op == 1 or op == 2:
                if op == 1:
                    self.capacidade_bateria = 40
                elif op == 2:
                    self.capacidade_bateria = 65
                break
        
    
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano):
        #inicializa toso os atributos da classe pai (Carro)
        super().__init__(marca, modelo, ano)
        self.bateria = Bateria()


