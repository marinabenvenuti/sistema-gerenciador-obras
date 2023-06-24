from herança_pedreiro import Pedreiro
salario_pedreiros = 1500 #melhorar essa variável, talvez pedir pra o usuario digitar quanto vai ganhar o pedreiro por obra
    
class Obra:
    def __init__(self, cod, cliente, materiaisusados, pedreiros, dataIn, dataFim, total):
        self.cod = cod
        self.cliente = cliente
        self.materiais = materiaisusados
        self.pedreiros = pedreiros
        self.dataIn = dataIn
        self.dataFim = dataFim
        self.total = total
        
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
        
    def addPedreiros(self, aux, pedreiros, pedreirosusados):
        for i in range(aux):
            aux2 = str(input('Digite o cpf do pedreiro: ')) #pesquisa por cpf, depois adicionar mais opções de pesquisa
            contador = 0
            if aux2 == #continuar depois
            
    def setPedreiros(self, pedreirosusados):
        self.pedreiros = pedreirosusados
            
    def setDataIn(self, dataIn):
        self.dataIn = dataIn
            
    def setDataFim(self, dataFim):
        self.dataFim = dataFim
        
    def calculaObra(pedreirosusados, materiaisusados):
        total = (len(pedreirosusados)*salario_pedreiros)+0.05*salario_pedreiros
        for i in range(len(materiaisusados)):
            for material in materiaisusados:
                total += material['qtd'] * material['preço']
                
        return total
    
    def setTotal(self, totalObra):
        self.total = totalObra
