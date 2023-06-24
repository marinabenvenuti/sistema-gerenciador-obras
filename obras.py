class Obra:
    def __init__(self, cod, cliente, materiaisusados, pedreiros, dataIn, dataFim, total):
        self.cod = cod
        self.cliente = cliente
        self.materiais = materiais
        self.total = total
        for i in range (len(self.materias)):
            print("O material", self.materiais[i]['nome'], "possui", self.materiais[i]['qtd'], "itens")
            add_num_mat=int(input("Quantos voce deseja adicionar? a medida é em {} com o valor de R${}".format(self.materiais[i]['medição'], self.materiais[i]['preço'])))
            self.materiais[i]['qtd']+=add_num_mat
            self.total+=(add_num_mat*self.materiais[i]['preço'])
            
        self.pedreiros = pedreiros
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
            
        return materiaisusados
                
    def setMateriais(self, materiaisusados):
        self.materiais = materiaisusados
        
    def setDataIn(self, dataIn):
        self.dataIn = dataIn
            
    def setDataFim(self, dataFim):
        self.dataFim = dataFim
        
    def setTotal(self, totalObra):
        self.total = totalObra
