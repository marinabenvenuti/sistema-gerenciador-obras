import random
funcionarios = []
pedreiros = []
gestores = []

class Funcionario:
    def __init__(self, Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, salarioTot):
        self.nome = Fun_Nome
        self.cpf = Fun_CPF
        self.fone = Fun_Fone
        self.cadastro = Fun_Cadastro
        self.salario = salarioTot
        
    def setNome(self, nome):
        self.nome = nome
    
    def setCPF(self, cpf):
        self.cpf = cpf
        
    def setFone(self, fone):
        self.fone = fone
        
    def setCadastro(self, cadastro):
        self.cadastro = cadastro
        
    def calculaSalario(self, salario):
        
    
        
class Gestor(Funcionario):    
    def __init__(self, Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, salarioTot, contra):
        super().__init__(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, salarioTot)
        self.contra= anoContrat
        gestores.append(self)
        funcionarios.append(self)
        
    def calculaSalario(self, salario):
        salarioTot = salario+(500*(2023-self.contra))
        return salarioTot
        
        
    def setContra(self, contratacao):
        self.contra = contratacao
        
class Pedreiro(Funcionario):
    def __init__(self, Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, salarioTot):
        super().__init__(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, salarioTot)        
        self.NumObras=0
        funcionarios.append(self)
        pedreiros.append(self)
        
    def calculaSalario(self, salario):
        salarioTot = salario+(350*(self.NumObras))
        return salarioTot
        
