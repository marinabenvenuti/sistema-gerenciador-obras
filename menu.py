from funcionarios import Funcionario
from obras import Obra

def verconsul(x):
    while not x in ["1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]:
        x=input("Digite novamente o número da ação: ")
    return x
                
#main

obras = []
funcionarios = []
pedreiros = []
pedreirosusados = []
materiais = []
materiaisusados = []
material = {}
material['nome'] = str('tijolo')
material['medição'] = str('unidade(s)')
material['qtd'] = int(0)
material['preço'] = float(25.00)
materiais.append(material.copy())

material = {}
material['nome'] = str('areia')
material['medição'] = str('m3')
material['qtd'] = int(0)
material['preço'] = float(170.00)
materiais.append(material.copy())

material = {}
material['nome'] = str('cal')
material['medição'] = str('kg')
material['qtd'] = int(0)
material['preço'] = float(13.00)
materiais.append(material.copy())

material = {}
material['nome'] = str('brita')
material['medição'] = str('m3')
material['qtd'] = int(0)
material['preço'] = float(96.00)
materiais.append(material.copy())

material = {}
material['nome'] = str('cimento')
material['medição'] = str('kg')
material['qtd'] = int(0)
material['preço'] = float(30.00)
materiais.append(material.copy())

material = {}
material['nome'] = str('telha de aço')
material['medição'] = str('m2')
material['qtd'] = int(0)
material['preço'] = float(20.00)
materiais.append(material.copy())

material = {}
material['nome'] = str('vergalhão')
material['medição'] = str('m')
material['qtd'] = int(0)
material['preço'] = float(16.00)
materiais.append(material.copy())

print ("  ")
print("[--------------------Sistema Gerenciador de Obras--------------------]")
print("[--------------------------------Menu--------------------------------]")
print("  ")
print("1) Ver todas as obras cadastradas")
print("2) Pesquisar obra")
print("3) Cadastrar obra")
print("4) Editar obra")
print("5) Excluir obra")
print("6) Ver lista de materiais disponíveis")
print("7) Pesquisar material")
print("8) Cadastrar material")
print("9) Editar material")
print("10) Excluir material")
print("11) Ver todos os funcionários cadastrados")
print("12) Pesquisar funcionário")
print("13) Cadastrar funcionário")
print("14) Editar funcionário")
print("15) Cadastrar funcionário")
print("16) Excluir funcionário")
print("17) Ver o faturamento atual da empresa")
print("18) Encerrar o programa")
print("  ")
    
consulta=input("Numero da ação a ser realizada: ")
ver_consul=verconsul(consulta)

if consulta==1:
    
    
elif consulta==2:
    print('Pesquisar obra')
    print('1 - Pesquisar pelo ID')
    print('2 - Pesquisar pelo nome do cliente')
    consulta2 = int(input('Escolha a forma de consulta: '))
        
    if consulta2 == 1: # Consultar pelo ID
        flag=False
        c = str(input('Digite o ID: '))
        for obr in obras:
            if c == func.get_cod():
                print('ID:', obr.get_cod())  # resgata os dados da obra
                print('Cliente:', obr.get_cliente())
                print('Materiais:', obr.get_materiais())
                print('Pedreiros:', obr.get_pedreiros())
                print('Data de início:', obr.get_dataIn())
                print('Data de fim:', obr.get_dataFim())
                print('Valor total:', obr.get_total())
                flag = True
            if flag == False:
                print("ID não cadastrado!")
                
                    
        elif consulta2 == 2: # Consultar pelo Nome
            c = str(input('Digite o nome do cliente: '))
            flag = False
            for obr in obras:
            if c == func.get_cod():
                print('ID:', obr.get_cod())  # resgata os dados da obra
                print('Cliente:', obr.get_cliente())
                print('Materiais:', obr.get_materiais())
                print('Pedreiros:', obr.get_pedreiros())
                print('Data de início:', obr.get_dataIn())
                print('Data de fim:', obr.get_dataFim())
                print('Valor total:', obr.get_total())
                flag = True
            if flag == False:
                print("Nome não cadastrado!")
                
elif colsulta==3:
    materiaisusados = []
    pedreirosusados = []
    print('Cadastro de obra')
        
    idO += 1
    cliente = str(input('Cliente: '))
    
    o = Obra('', '', '', '', '', '', '') # cria o objeto Obra
    o.set_cod(str(idO))
    o.set_cliente(cliente)
    
    aux = int(input('Digite a quantidade de materiais que serão utilizados: '))
    while aux>len(materiais)+1:
        aux = int(input('Valor inválido! Digite a quantidade de materiais que serão utilizados novamente: '))
    materiaisusados.append(addMateriais(aux, materiaisusados))
    
    o.set_materiais(materiaisusados)
    
    aux = int(input('Digite a quantidade de pedreiros que trabalharão na obra: '))
    while aux>len(pedreiros):
        aux = int(input('Valor inválido! digite a quantidade de pedreiros que trabalharão na obra novamente: '))
    #continuar depois
    
    

    obras.append(o)
