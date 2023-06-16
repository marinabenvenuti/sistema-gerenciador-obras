from funcionarios import funcionario
class Pedreiro(Funcionario):
    def __init__(self,nome, cpf, fone, salario):
        super().__init__(nome)
        self.cpf = cpf