#Marina Benvenuti Cardeal 23103131
#Iago Rodrigues Munoz 23104313
from funcionarios import *
obras = []
class Obra:
    def __init__(self, cod, cliente, materiais, total, nomePedr, dataIn, dataFim):
        self.cod = cod
        self.cliente = cliente
        self.materiais = materiais
        self.total = 0 
        self.pedreiro = nomePedr
        self.dataIn = dataIn
        self.dataFim = dataFim
                  
    def setCliente(self, cliente):
        self.cliente = cliente

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
        
    def setTotalRem(self, totalObra):
        self.total -= totalObra
        
    def setTotal(self, totalObra):
        self.total += totalObra
