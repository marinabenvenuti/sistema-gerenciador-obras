from datetime import datetime
from funcionarios import Funcionario
from obras import Obra

def verConsul(x):
    while not x in ["1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]:
        x=input("Digite novamente o número da ação: ")
    return x

def verificaData(aux):
    verif = 0
    for i in range(10):
        #fazer função pra verificar se a data está certa
                
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
material['qtd'] = int(0) #arrumar essa qtd dos materiais, fazer código q tenha um estoque e a cada obra diminua 
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

while True:
    print ("  ")
    print("[--------------------Sistema Gerenciador de Obras--------------------]")
    print("[--------------------------------Menu--------------------------------]")
    print("  ")
    print("1) Ver todas as obras cadastradas") #iago?
    print("2) Pesquisar obra") #marina
    print("3) Cadastrar obra") #marina
    print("4) Editar obra") #marina
    print("5) Excluir obra") #marina
    print("6) Ver lista de materiais disponíveis") #iago?
    print("7) Pesquisar material") #marina
    print("8) Cadastrar material") #marina (ver sobra estoque!!!!!)
    print("9) Editar material")
    print("10) Excluir material")
    print("11) Ver todos os funcionários cadastrados") #iago?
    print("12) Pesquisar funcionário")
    print("13) Cadastrar funcionário")
    print("14) Editar funcionário")
    print("15) Cadastrar funcionário")
    print("16) Excluir funcionário")
    print("17) Ver o faturamento atual da empresa")
    print("18) Encerrar o programa")
    print("  ")
        
    consulta=input("Numero da ação a ser realizada: ")
    ver_consul=verConsul(consulta)

    if consulta==1:
        for i in obras:
            print (' ')
            if i<10:
                print ('Obra 0{}'.format(i+1))
            else:
                print ('Obra {}'.format(i))
            print ('Codigo da obra:', i.cod)
            print ('Cliente:', i.cliente)
            print ('Inicio da obra:', i.dataIn)
            print('Fim da obra:', i.dataFim)
        
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
            
        idO += 1 #olhar melhor esse id
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
        pedreirosusados.append(addPedreiros(aux, pedreirosusados))
        o.set_pedreiros(pedreirosusados)
        #continuar depois
        
        aux = str(input('Digite a data de início da obra no formado "DD/MM/AAAA": '))
        data_inicio = verificaData(aux)
        dataIn = datetime.strptime(data_inicio, '%d/%m/%Y')
        o.set_dataIn(dataIn)
        
        aux = str(input('Digite a data de fim da obra no formado "DD/MM/AAAA": '))
        data_fim = verificaData(aux)
        dataFim = datetime.strptime(data_fim, '%d/%m/%Y')
        o.set_dataFim(dataFim)
        
        totalObra = calculaObra(pedreirosusados, materiaisusados)
        o.set_total(totalObra)
        
        obras.append(o) #adicionando à lista de objetos obra
        
    elif consulta==4:
        print('Alterar informação de obra')
        idO_pesquisa = str(input('Digite o ID da obra: '))
        flag=False
        for obra in obras:  # percorre a lista de funcionários
            if idO_pesquisa == obra.get_cod():  # busca pelo ID da obra a ser alterado
                materiaisusados = []
                pedreirosusados = []
                print('Digite as novas informações de obra')
                cliente = str(input('Cliente: '))
                obra.set_cliente(cliente)
                
                aux = int(input('Digite a quantidade de materiais que serão utilizados: '))
                while aux>len(materiais)+1:
                    aux = int(input('Valor inválido! Digite a quantidade de materiais que serão utilizados novamente: '))
                materiaisusados.append(addMateriais(aux, materiaisusados))
                obra.set_materiais(materiaisusados)
                
                aux = int(input('Digite a quantidade de pedreiros que trabalharão na obra: '))
                while aux>len(pedreiros):
                    aux = int(input('Valor inválido! digite a quantidade de pedreiros que trabalharão na obra novamente: '))
                pedreirosusados.append(addPedreiros(aux, pedreirosusados))
                obra.set_pedreiros(pedreirosusados)
                
                aux = str(input('Digite a data de início da obra no formado "DD/MM/AAAA": '))
                data_inicio = verificaData(aux)
                dataIn = datetime.strptime(data_inicio, '%d/%m/%Y')
                obra.set_dataIn(dataIn)
        
                aux = str(input('Digite a data de fim da obra no formado "DD/MM/AAAA": '))
                data_fim = verificaData(aux)
                dataFim = datetime.strptime(data_fim, '%d/%m/%Y')
                obra.set_dataFim(dataFim)
        
                totalObra = calculaObra(pedreirosusados, materiaisusados)
                obra.set_total(totalObra)
                
                flag=True
            if flag == False:
                print("ID não encontrado!")
                
    elif consulta==5:
        print('Excluir obra')
        idO_pesquisa = str(input('Digite o ID da obra: '))
        
        for i, j in enumerate(obras): # percorre a lista de obras
            if idO_pesquisa == j.get_cod():
                obras.pop(i)
                print("Exclusão efetuada com sucesso!")
                flag=True
        if flag == False:
            print("Id não cadastrado!")
            
    elif consulta==6:
        #ver lista de materiais disponíveis
        #continuar
        
    elif consulta==7:
        #pesquisar material no dicionário por nome
        print('Pesquisar material')
        flag = False
        aux = input('Digite o nome do material: ')
        for material in materiais:
            if material['nome'] == aux:
                print('Nome: ', material['nome'])
                print('Medido por: ', material['medição'])
                print('Preço: R$', material['preço'])
                flag = True
                #ver sobre estoque
        if flag = False:
            print('Material não encontrado!')
            
    elif consulta==8:
        #cadastrar material novo no dicionário (ver sobre cadastrar estoque de materiais)
        print('Cadastro de novo material')
        material = {}
        material['nome'] = str(input('Digite o nome do material: '))
        material['medição'] = str(input('Digite a forma de medição do material: '))
        material['qtd'] = int(0)
        material['preço'] = float(input('Digite o preço do material, à partir da forma de medição: '))
        materiais.append(material.copy())
        print('Material cadastrado com sucesso!')
        
    elif consulta==9:
        #editar material no dicionário de materiais
        print('Alterar informações de material')
        nomeMat = input('Digite o nome do material: ')
        flag = False
        for material in materiais:
            if material['nome'] == nomeMat:
                material = {}
                material['nome'] = str(input('Digite o nome do material: '))
        material['medição'] = str(input('Digite a forma de medição do material: '))
        material['qtd'] = int(0)
        material['preço'] = float(input('Digite o preço do material, à partir da forma de medição: '))
        materiais.append(material.copy())

    elif consulta==10:



    elif consulta==11:



    elif consulta==12:



    elif consulta==13:
        

 