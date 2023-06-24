from obras import *
from funcionarios import *

def printarObra(i):
    print(' ')
    print('ID:', i.get_cod())  
    print('Cliente:', i.get_cliente())
    print('Materiais:', i.get_materiais())
    print('Mestre de obra:', i.get_pedreiro())
    print('Data de início:', i.get_dataIn())
    print('Data de fim:', i.get_dataFim())
    print('Valor total:', i.get_total())
    
#def verificaData(aux):
 #   verif = 0
  #  for i in range(10):
   #     #fazer função pra verificar se a data está certa
    

def verConsul(x):
    while not x in ["1","2", "3", "4", "5", "6"]:
        x=input("Digite novamente o número da ação: ")
    return x

def opcoesObras():
    while True:
        print("[--------------------------------Menu de Obras--------------------------------]")
        print("  ")
        print("1) Exibir todas as obras cadastradas")
        print("2) Pesquisar obra")
        print("3) Cadastrar obra")
        print("4) Editar obra")
        print("5) Excluir obra")
        print("6) Voltar para o menu principal")
        print("  ")
            
        consultaObra=input("Numero da ação a ser realizada: ")
        consultaObra=verConsul(consulta)
        
        if consultaObra==1:
            if obras==[]:
                print('Nenhuma obra cadastrada')
            else:
                print('--------------------------------Obras cadastradas:--------------------------------')
                ContObras=0
                for i in obras:
                    ContObras+=1
                    printarObra(i)
                    
        if consultaObra==2:
            #pesquisa de obra específica
            if obras==[]:
                print('Nenhuma obra cadastrada')
            else:
                print('--------------------------------Pesquisar obra:--------------------------------')
                print('1 - Pesquisar pelo ID')
                print('2 - Pesquisar pelo nome do cliente')
                consulta2 = int(input('Escolha a forma de consulta: '))
                    
                if consulta2 == 1: # Consultar pelo ID
                    flag=False
                    c = str(input('Digite o ID: '))
                    for obr in obras:
                        if c == func.get_cod():
                            printarObra(obr)
                            flag = True
                        if flag == False:
                            print("ID não cadastrado!")
                            
                                
                elif consulta2 == 2: # Consultar pelo Nome
                    c = str(input('Digite o nome do cliente: '))
                    flag = False
                    for obr in obras:
                        if c == func.get_cod():
                            printarObra(obr)
                            flag = True
                        if flag == False:
                            print("Nome não cadastrado!")
                            
        if consultaObra==3:
            #cadastro de nova obra
            materiais = []

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
            
            print('--------------------------------Cadastrar obra:--------------------------------')
                
            cliente = str(input('Cliente: ')).title
            
            o = Obra('', '', '', '', '', '', '') # cria o objeto Obra
            o.set_cod(random.randint(10000, 100000))
            o.set_cliente(cliente)
            
            o.set_materiais(materiaisusados)



            
            flag = False
            while True: #isso pode ser colocado numa função pois é usado na edição também
                nomePedr = input('Digite o nome completo do mestre de obra: ').title
                for pedreiro in pedreiros:
                    if nomePedr == pedreiro.nome:
                        o.set_pedreiro(nomePedr)
                        flag = True
                if flag==True:
                    break
            
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
            
        if consultaObra == 4:
            print('--------------------------------Editar obra:--------------------------------')
            idO_pesquisa = str(input('Digite o ID da obra: '))
            flag=False
            for obra in obras:  # percorre a lista de obras
                if idO_pesquisa == obra.get_cod():  # busca pelo ID da obra a ser alterado
                    materiaisusados = []
                    print('Digite as novas informações de obra')
                    cliente = str(input('Cliente: ')).title
                    obra.set_cliente(cliente)
                    
                    aux = int(input('Digite a quantidade de materiais que serão utilizados: '))
                    while aux>len(materiais)+1:
                        aux = int(input('Valor inválido! Digite a quantidade de materiais que serão utilizados novamente: '))
                    materiaisusados.append(addMateriais(aux, materiaisusados))
                    obra.set_materiais(materiaisusados)
                    
                    flagg = False
                    while True:
                        nomePedr = input('Digite o nome completo do mestre de obra: ').title
                        for pedreiro in pedreiros:
                            if nomePedr == pedreiro.nome:
                                o.set_pedreiro(nomePedr)
                                flagg = True
                        if flagg==True:
                            break
                    
                    aux = str(input('Digite a data de início da obra no formado "DD/MM/AAAA": '))
                    data_inicio = verificaData(aux)
                    dataIn = datetime.strptime(data_inicio, '%d/%m/%Y')
                    obra.set_dataIn(dataIn)
            
                    aux = str(input('Digite a data de fim da obra no formado "DD/MM/AAAA": '))
                    data_fim = verificaData(aux)
                    dataFim = datetime.strptime(data_fim, '%d/%m/%Y')
                    obra.set_dataFim(dataFim)
            
                    totalObra = calculaObra(pedreirosusados, materiaisusados) #arrumar
                    obra.set_total(totalObra)
                    
                    flag=True
                if flag == False:
                    print("ID não encontrado!")
                    
        if consultaObra == 5:
            #exclusão de obra
            print('--------------------------------Excluir obra:--------------------------------')
            idO_pesquisa = str(input('Digite o ID da obra: '))
            
            for i, j in enumerate(obras): # percorre a lista de obras
                if idO_pesquisa == j.get_cod():
                    obras.pop(i)
                    print("Exclusão efetuada com sucesso!")
                    flag=True
            if flag == False:
                print("Id não cadastrado!")
                
        if consultaObra == 6:
            break
        
def opcoesMateriais():
    while True:
        print("[--------------------------------Menu de Materiais--------------------------------]")
        print("  ")
        print("1) Exibir todos os materiais cadastrados")
        print("2) Pesquisar material")
        print("3) Cadastrar material")
        print("4) Editar material")
        print("5) Excluir material")
        print("6) Voltar para o menu principal")
        print("  ")
            
        consultaMaterial=input("Numero da ação a ser realizada: ")
        consultaMaterial=verConsul(consulta)
        
        if consultaMaterial==1:
            print("[--------------------------------Lista de Materiais--------------------------------]")
            #fazer
            
        if consultaMaterial==2:
            print("[--------------------------------Pesquisar materiais--------------------------------]")
            flag = False
            aux = input('Digite o nome do material: ')
            for material in materiais:
                if material['nome'] == aux:
                    print('Nome: ', material['nome'])
                    print('Medido por: ', material['medição'])
                    print('Preço: R$', material['preço'])
                    flag = True
                    #ver sobre estoque
            if flag == False:
                print('Material não encontrado!')
                
        if consultaMaterial==3:
            #cadastrar material novo no dicionário (ver sobre cadastrar estoque de materiais)
            print("[--------------------------------Cadastrar materiais--------------------------------]")
            material = {}
            material['nome'] = str(input('Digite o nome do material: '))
            material['medição'] = str(input('Digite a forma de medição do material: '))
            material['qtd'] = int(0)
            material['preço'] = float(input('Digite o preço do material, à partir da forma de medição: '))
            materiais.append(material.copy())
            print('Material cadastrado com sucesso!')
            
        if consultaMaterial==4:
            #editar material no dicionário de materiais
            print("[--------------------------------Editar material--------------------------------]")
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
                    flag = True
            if flag == False:
                print('Material não encontrado')
                
        if consultaMaterial==5:
            #excluir material no dicionário de materiais
            print("[--------------------------------Excluir material--------------------------------]")
            nomeMat = input('Digite o nome do material: ')
            flag = False
            for material in materiais:
                if material['nome'] == nomeMat:
                    materiais.remove(material)
                    flag = True
            if flag == False:
                print('Material não encontrado')
            
        if consultaMaterial==6:
            break
        
def opcoesFuncionarios():
    while True:
        print("[--------------------------------Menu de Funcionários--------------------------------]")
        print("  ")
        print("1) Exibir todos os funcionários cadastrados")
        print("2) Pesquisar funcionário")
        print("3) Cadastrar funcionário")
        print("4) Editar funcionário")
        print("5) Excluir funcionário")
        print("6) Voltar para o menu principal")
        print("  ")
            
        consultaFunc=input("Numero da ação a ser realizada: ")
        consultaFunc=verConsul(consulta)
        
        if consultaFunc==1:
            #exibir todos os funcionários da empresa
            if funcionarios==[]:
                print('Nenhum funcionário cadastrado')
            
            else:
                print("[--------------------------------Funcionários cadastrados:--------------------------------]")
                for i in funcionarios:
                    print ("   ")
                    print ('Cargo:', i.__class__.__name__)
                    print ('Cadastro:', i.cadastro)
                    print ('Nome:', i.nome)
                    print ('Salario: R${}'.format(i.Sal_Calc))
                    print ('CPF: {}.{}.{}-{}'.format(i.cpf[0:3], i.cpf[3:6], i.cpf[6:9], i.cpf[9:11]))
                    print ('Contato: {}-{}'.format(i.fone[0:5], i.fone[5:9]))

                    if i.__class__.__name__=='Gestor':
                        print ('Data contrataçao:', i.contra)
                    if i.__class__.__name__=='Pedreiro':
                        print ('Presente em {} obras'.format(i.NumObras))
                        
        if consultaFunc==2:
            #pesquisa de funcionário específico
            print("[--------------------------------Pesquisar funcionário:--------------------------------]")
            Pes_Fun=input('Nome do funcionario a ser pesquisado: ').title()
            for i in funcionarios:
                if i.nome==Pes_Fun:
                    print ("   ")
                    print ('Cargo:', i.__class__.__name__)
                    print ('Cadastro:', i.cadastro)
                    print ('Nome:', i.nome)
                    print ('Salario: R${}'.format(i.Sal_Calc))
                    print ('CPF: {}.{}.{}-{}'.format(i.cpf[0:3], i.cpf[3:6], i.cpf[6:9], i.cpf[9:11]))
                    print ('Contato: {}-{}'.format(i.fone[0:5], i.fone[5:9]))
                    
                    if i.__class__.__name__=='Gestor':
                        print ('Data contrataçao:', i.contra)
                    if i.__class__.__name__=='Pedreiro':
                        print ('Presente em {} obras'.format(i.NumObras))
                        
        if consultaFunc==3:
            #cadastro de novo funcionário
            print("[--------------------------------Cadastrar funcionário:--------------------------------]")
            print(' ')
            Pes_Fun=input('Nome do funcionario a ser pesquisado: ').title()

            Faz_Cad=input('O que deseja cadastrar? ').title()   
            Fun_Nome=input('Nome do Funcionario: ').title()
            Fun_CPF=input('CPF do funcionario[sem"." e "-"]: ')
            Fun_Fone=input('Telefone do Funcionario[Com "9" e sem DDD]: ')
            Fun_Cadastro=(random.randint(10000,100000))
            Fun_Salario=1000
            
            if Faz_Cad=='Gestor':
                Gestor(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario)

            elif Faz_Cad=='Pedreiro':
                Pedreiro(Fun_Nome, Fun_CPF, Fun_Fone, Fun_Cadastro, Fun_Salario)
                
        if consultaFunc==4:
            #edição de funcionário
            print("[--------------------------------Editar funcionário:--------------------------------]")
            print(' ')
            editFunc = input('Digite o nome completo do funcionário a ser editado: ')
            for i in funcionarios:
                if i.nome == editFunc:
                    nome = input('Digite o novo nome do funcionário: ')
                    i.set_nome(nome)
                    
                    cpf = input('Digite o novo cpf do funcionário: ')
                    i.set_cpf(cpf)
                    
                    fone = input('Digite o novo telefone do funcionário: ')
                    i.set_fone(fone)
                    
                    if i.__class__.__name__=='Gestor':
                        contratacao = int(input('Digite o novo ano de contratação do funcionário: '))
                        i.set_contra(contratacao)
                        
        if consultaFunc==5:
            #exclusão de funcionário
            print("[--------------------------------Excluir funcionário:--------------------------------]")
            print('   ')
            Del_Fun=input('Digite o nome completo do funcionario a ser excluido: ').title()
            for i in funcionarios:
                if i.nome==Del_Fun:
                    print ("   ")
                    print ('Cargo:', i.__class__.__name__)
                    print ('Cadastro:', i.cadastro)
                    print ('Nome:', i.nome)
                    print ('Salario: R${}'.format(i.Sal_Calc))
                    print ('CPF: {}.{}.{}-{}'.format(i.cpf[0:3], i.cpf[3:6], i.cpf[6:9], i.cpf[9:11]))
                    print ('Contato: {}-{}'.format(i.fone[0:5], i.fone[5:9]))
                    
                    if i.__class__.__name__=='Gestor':
                        print ('Data contrataçao:', i.contra)
                    if i.__class__.__name__=='Pedreiro':
                        print ('Presente em {} obras'.format(i.NumObras))

                    print('   ')
                    Del_Fun_F=input('Excluir este funcionario?').title()
                    if Del_Fun_F=='sim':
                        funcionarios.pop(i)
                        print('Funcionário deletado com sucesso')
                else:
                    print('Funcionário não cadastrado')
                    
        if consultaFunc==6:
            break
        
def faturamento():
    #fazer
    print("[--------------------------------Faturamento atual:--------------------------------]")
    
def consultaMain(x):
    while not x in ["1","2", "3", "4", "5"]:
        x=input("Digite novamente o número da ação: ")
    return x

#main
while True:
    print ("  ")
    print("[--------------------Sistema Gerenciador de Obras--------------------]")
    print("[--------------------------------Menu--------------------------------]")
    print("  ")
    print("1) Obras")
    print("2) Materiais")
    print("3) Funcionários")
    print("4) Faturamento da empresa")
    print("5) Encerrar programa")
    print("  ")
        
    consulta=input("Numero da ação a ser realizada: ")
    consulta=consultaMain(consulta)
    
    if consulta == 1:
        opcoesObras()
        
    elif consulta == 2:
        opcoesMateriais()
            
    elif consulta == 3:
        opcoesFunc()
        
    elif consulta == 4:
        faturamento()
    
    elif consulta == 5:
        break
