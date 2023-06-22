class Funcionario:
    def __init__(self, nome, sobrenome, cpf, fone, salario, cadastro):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.fone = fone
        self.salario = salario
        self.cadastro = cadastro
        
class Gestor(Funcionario):
    def __init__(self, nome, sobrenome, cpf, fone, salario, dataContratacao):
        super().__init__(nome, sobrenome, cpf, fone, salario)
        self.dataContratacao = dataContratacao
        
    def getDataContratacao(self):
        return self.dataContratacao
    
    def setDataContratacao(self, dataContratacao):
        self.dataContratacao = dataContratacao
        
class Pedreiro(Funcionario):
    def __init__(self, nome, sobrenome, cpf, fone, salario, qtdObras):
        super().__init__(nome, sobrenome, cpf, fone, salario)
        self.qtdObras = qtdObras
        
    def getQtdObras(self):
        return self.qtdObras
    
    def setQtdObras(self, qtdObras):
        self.qtdObras = qtdObras
