from classes_02 import Usuario

class Privilegios:
    def __init__(self):
        self.privilegios = ['Cadastrar Usuários', 'Deletar Posts', 'Confugurações Gerais']
    def get_privilegios(self):
        #Retorna a lista de privilegios do usuário
        return self.privilegios


class Admin (Usuario):
    #Usuário é um tipo especial de usuário então poser se uma classe filha de usuário
    def __init__(self, nome, sobrenome):
        #Inicializa os atributos da Classe Pai (usuario)
        super().__init__(nome, sobrenome)
        self.permissoes = Privilegios()