#Exercício 9.3
class Usuario:
    def __init__(self, nome, sobrenome):
        #Inicializa os atributos nome e sobrenome
        self.nome = nome
        self.sobrenome = sobrenome
    
    def descricao_usuario(self):
        #Exibe na tela o nome e o sobrenome do usuário
        print(f'{self.nome} {self.sobrenome}')

    def cumprimenta_usuario(self):
        #Exibe uma mensagem de boas vindas ao usuário
        print(f'Seja bem vindo {self.nome}')


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