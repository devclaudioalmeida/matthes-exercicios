#Exercício 9.3, 9.5
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




usuario_01 = Usuario('Cláudio', 'Almeida')
usuario_02 = Usuario('José', 'Almeida')
usuario_03 = Usuario('Antônio', 'Almeida')
print('*' * 60)
usuario_01.descricao_usuario()
usuario_02.descricao_usuario()
usuario_03.descricao_usuario()
print('*' * 60)
usuario_01.cumprimenta_usuario()
usuario_02.cumprimenta_usuario()
usuario_03.cumprimenta_usuario()
print('*' * 60)
print(f'O usuário {usuario_02.nome} tentou logar {usuario_02.get_tentativas_login()} vezes no sistema!')
usuario_02.incremeta_tentativas_login()
usuario_02.incremeta_tentativas_login()
usuario_02.incremeta_tentativas_login()
usuario_02.incremeta_tentativas_login()
print('*' * 60)
print(f'O usuário {usuario_02.nome} tentou logar {usuario_02.get_tentativas_login()} vezes no sistema!')
usuario_02.reset_tentativas_login()
print('*' * 60)
print(f'O usuário {usuario_02.nome} tentou logar {usuario_02.get_tentativas_login()} vezes no sistema!')