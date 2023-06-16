from herança_pedreiro import Pedreiro
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
        
    def addMateriais(self, aux, materiais, materiaisusados):
        for i in range(aux):
            aux2 = str(input('Digite o nome do material necessário: '))
            contador = 0
            for material in materiais:
                if material['nome'] == aux2:
                    qtd = int(input('Digite a quantidade do material, utilizando apenas números: '))
                    material['qtd'] = qtd
                    materiaisusados.append(material)
                    contador += 1
            if contador<1:
                aux2 = str(input('Material não encontrado! Digite o nome do material necessário novamente: ')) #aqui deve-se encontrar uma solução pra que o primeiro for continue tendo a quantidade dada pelo aux
        return materiaisusados
                
    def setMateriais(self, materiaisusados):
        self.materiais = materiaisusados
        
    def addPedreiros(self, aux, pedreiros, pedreirosusados):
        for i in range(aux):
            aux2 = str(input('Digite o nome do pedreiro: '))
            contador = 0
            if aux2 == #continuar depois
            
        
                    
        
        