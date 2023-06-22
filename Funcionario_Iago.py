import random
funcionarios = []
pedreiros = []
gestores = []

class Funcionario:
    def __init__(self, Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario):
        self.nome = Fun_Nome
        self.cpf = Fun_CPF
        self.fone = Fun_Fone
        self.cadastro = Fun_Cadastro
        self.salario = Fun_Salario
        
        
class Gestor(Funcionario):
    
    def __init__(self, Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario):
        super().__init__(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario)
        
        self.contra= int(input('Data da contrataçao[AAAA]: '))
        self.Sal_Calc=(self.salario+(500*(2023-self.contra)))
        gestores.append(self)
        funcionarios.append(self)
        
class Pedreiro(Funcionario):
    def __init__(self, Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario):
        super().__init__(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario)
        
        self.NumObras=0
        self.Sal_Calc=(self.salario+(350*(self.NumObras)))
        funcionarios.append(self)
        pedreiros.append(self)
