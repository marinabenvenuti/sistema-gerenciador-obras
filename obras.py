from funcionarios import *
obras = []
class Obra:
    def __init__(self, cod, cliente, materiais, nomePedr, dataIn, dataFim, total):
        self.cod = cod
        self.cliente = cliente
        self.materiais = materiais
        self.total = total
            
        self.pedreiro = nomePedr
        self.dataIn = dataIn
        self.dataFim = dataFim
        
        
    def getCod(self):
        return self.cod
    
    def getCliente(self):
        return self.cliente
    
    def setCod(self, cod):
        self.cod = cod
        
    def setCliente(self, cliente):
        self.cliente = cliente
        
    def addMateriais(self):
        
        for i in range (len(self.materias)):
            print("O material", self.materiais[i]['nome'], "possui", self.materiais[i]['qtd'], "itens")
            add_num_mat=int(input("Quantos voce deseja adicionar? a medida é em {} com o valor de R${}".format(self.materiais[i]['medição'], self.materiais[i]['preço'])))
            self.materiais[i]['qtd']+=add_num_mat
            self.total+=(add_num_mat*self.materiais[i]['preço'])
            
                            
    def setMateriais(self, materiais):
        self.materiais = materiais
            
    def setPedreiro(self, nomePedr):
        self.pedreiro = nomePedr
            
    def setDataIn(self, dataIn):
        self.dataIn = dataIn
        
    def setCod(self, cod):
        self.cod = cod
            
    def setDataFim(self, dataFim):
        self.dataFim = dataFim
        
    def calculaObra(self, materiais):
        total = 350*1.22
        for i in materiais:
            total += material['qtd'] * material['preço']
                
        return total
    
    def setTotal(self, totalObra):
        self.total = totalObra
