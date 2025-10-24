#Exercício 9.3, 9.5, 9.7, 9.8
class Usuario:
    def __init__(self, nome, sobrenome):
        #Inicializa os atributos nome e sobrenome
        self.nome = nome
        self.sobrenome = sobrenome
        self.tentativas_login = 0
    
    def descricao_usuario(self):
        #Exibe na tela o nome e o sobrenome do usuário
        print(f'{self.nome} {self.sobrenome}')

    def cumprimenta_usuario(self):
        #Exibe uma mensagem de boas vindas ao usuário
        print(f'Seja bem vindo {self.nome}')

    #A partir daqui começa a solução do exercício 9.5
    def incremeta_tentativas_login(self):
        #incrementa as tentativas de login em 1 unidade
        self.tentativas_login += 1
    
    def reset_tentativas_login(self):
        #Reinicia o contador de tentativas de login
        self.tentativas_login = 0
    
    def get_tentativas_login(self):
        #Retorna o número de tentativas de login
        return self.tentativas_login





