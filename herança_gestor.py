from funcionarios import funcionario
class Gestor(Funcionario):
    def __init__(self, nome, cpf, fone, salario, dataContratacao):
        super().__init__(nome, cpf, fone, salario)
        self.dataContratacao = dataContratacao
        
    def getDataContratacao(self):
        return self.dataContratacao
    
    def setDataContratacao(self, dataContratacao):
        self.dataContratacao = dataContratacao
